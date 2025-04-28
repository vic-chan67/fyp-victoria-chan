# cropping.py
# Crop detected road signs from images to be passed to the CNN model

from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model
model = YOLO("py-files/runs/detect/train4/weights/best.pt")

def detect_and_crop(image_path, save_dir="cropped-signs"):
    image = cv2.imread(image_path)
    results = model(image_path)

    # Check save directory exists
    base_filename = os.path.splitext(os.path.basename(image_path))[0]
    out_dir = os.path.join(save_dir, base_filename)
    os.makedirs(out_dir, exist_ok=True)

    sign_index = 0
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_id = int(box.cls[0])
            #confidence = float(box.conf[0])

            # Crop the detected region
            cropped_sign = image[y1:y2, x1:x2]

            # Save the cropped sign
            crop_filename = f"{base_filename}_sign{sign_index}_cls{class_id}.jpg"
            crop_path = os.path.join(out_dir, crop_filename)
            cv2.imwrite(crop_path, cropped_sign)
            print(f"Saved cropped sign")
            sign_index += 1

    if sign_index == 0:
        print("No signs detected")
    else:
        print(f"Sign cropped and saved")

if __name__ == "__main__":
    detect_and_crop("datasets/gtsdb-data/00000.ppm")

