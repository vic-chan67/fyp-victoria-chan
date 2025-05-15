# gtsdb_yolo.py
# Convert GTSDB raw dataset to YOLO format (used for training)

import os
import random
import cv2

# Set these paths
GTSDB_IMAGE_DIR = "gtsdb-data/"  # GTSDB ppm images
ANNOTATION_FILE = "gtsdb-data/gt.txt"  # GTSDB annotations file
YOLO_DATASET_DIR = "gtsdb-yolo/"

# YOLO expects: dataset/images/train, dataset/labels/train, etc.
IMG_OUT = os.path.join(YOLO_DATASET_DIR, "images")
LBL_OUT = os.path.join(YOLO_DATASET_DIR, "labels")

# Create YOLO folder structure
for split in ["train", "val"]:
    os.makedirs(os.path.join(IMG_OUT, split), exist_ok=True)
    os.makedirs(os.path.join(LBL_OUT, split), exist_ok=True)

# Read annotation file
with open(ANNOTATION_FILE, "r") as f:
    lines = f.readlines()

annotations = {}

# Format: filename; x1; y1; x2; y2; class_id
for line in lines:
    parts = line.strip().split(";")
    filename = parts[0]
    bbox = list(map(int, parts[1:5]))
    class_id = int(parts[5])

    if filename not in annotations:
        annotations[filename] = []
    annotations[filename].append((bbox, class_id))

# Shuffle and split dataset
image_files = list(annotations.keys())
random.shuffle(image_files)
split_index = int(0.8 * len(image_files))
train_files = image_files[:split_index]
val_files = image_files[split_index:]

def convert_to_yolo(bbox, img_w, img_h):
    x1, y1, x2, y2 = bbox
    x_center = (x1 + x2) / 2 / img_w
    y_center = (y1 + y2) / 2 / img_h
    width = (x2 - x1) / img_w
    height = (y2 - y1) / img_h
    return x_center, y_center, width, height

def process_and_save(split, files):
    for filename in files:
        img_path = os.path.join(GTSDB_IMAGE_DIR, filename)
        if not os.path.exists(img_path):
            continue

        img = cv2.imread(img_path)
        h, w, _ = img.shape

        # Copy image
        split_img_path = os.path.join(IMG_OUT, split, filename.replace(".ppm", ".jpg"))
        cv2.imwrite(split_img_path, img)

        # Write label
        label_path = os.path.join(LBL_OUT, split, filename.replace(".ppm", ".txt"))
        with open(label_path, "w") as f:
            for bbox, class_id in annotations[filename]:
                x, y, w_norm, h_norm = convert_to_yolo(bbox, w, h)
                f.write(f"{class_id} {x:.6f} {y:.6f} {w_norm:.6f} {h_norm:.6f}\n")

print("Splitting training and validation data")
process_and_save("train", train_files)
process_and_save("val", val_files)
print("GTSDB converted to YOLO format")
