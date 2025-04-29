# detection.py
# Use YOLOv8 to detect road signs in images

from ultralytics import YOLO
import cv2
# import os
from descriptions import DESCRIPTIONS

# Load YOLOv8 model
model = YOLO("py-files/runs/detect/train4/weights/best.pt")

def detect_signs(image_path):  #take image path as input
    image = cv2.imread(image_path)
    results = model(image)  #pass image to YOLOv8 for prediction

    bounding_boxes = []
    for r in results:  #loop through results (r is a result object)
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  #get bounding box coords
            class_id = int(box.cls[0])  #get class id (sign type)
            #confidence = float(box.conf[0])  #get confidence score
            label = DESCRIPTIONS.get(class_id, f"Class {class_id}")  #get label from dictionary
            bounding_boxes.append((x1, y1, x2, y2, class_id, label))

            # Draw bounding box and label
            # cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # cv2.putText(image, label, (x1, y1 - 10),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    return image, bounding_boxes

    # # Save output image
    # out_path = image_path.replace("gtsdb-data", "detect-data").replace(".ppm", "_yolo.jpg")
    # os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # cv2.imwrite(out_path, image)
    # print(f"Output image saved")

if __name__ == "__main__":
    image, bounding_boxes = detect_signs("datasets/gtsdb-yolo/images/val/00090.jpg")
    print(f"Detected {len(bounding_boxes)} signs")
