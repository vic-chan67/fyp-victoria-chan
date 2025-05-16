# detection.py
# Use YOLOv8 to detect road signs in images

from ultralytics import YOLO
import cv2
import os
from descriptions import DESCRIPTIONS

# Dynamic path for the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_yolo", "weights", "best.pt")

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

def detect_signs(image_path):  #take image path as input
    image = cv2.imread(image_path)
    results = model(image)  #pass image to YOLOv8 for prediction

    bounding_boxes = []
    for r in results:  #loop through results (r is a result object)
        boxes = r.boxes
        for b in boxes:
            x1, y1, x2, y2 = map(int, b.xyxy[0])  #get bounding box coords
            class_id = int(b.cls[0])  #get class id (sign type)
            #confidence = float(box.conf[0])  #get confidence score
            label = DESCRIPTIONS.get(class_id, f"Class {class_id}")  #get label from dictionary
            bounding_boxes.append((x1, y1, x2, y2, class_id, label))

            # Draw bounding box and label
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Save output image
    output_dir = "py-files/detection-results"
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.basename(image_path).replace(".ppm", ".jpg")
    out_path = os.path.join(output_dir, base_name)
    cv2.imwrite(out_path, image)
    print(f"Output image saved to {out_path}")

    return image, bounding_boxes

if __name__ == "__main__":
    image, bounding_boxes = detect_signs("datasets/gtsdb-yolo/images/val/00090.jpg")
    print(f"Detected {len(bounding_boxes)} signs")
