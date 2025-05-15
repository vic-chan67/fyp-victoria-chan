# cropping.py
# Crop detected road signs from images to be passed to the CNN model

from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("py-files/runs/detect/train4/weights/best.pt")

def crop_signs(image, bounding_boxes):
    cropped_signs = []
    for idx, (x1, y1, x2, y2, class_id, label) in enumerate(bounding_boxes):
        cropped = image[y1:y2, x1:x2]
        cropped_signs.append({
            "image": cropped,
            "class_id": class_id,
            "label": label,
            "bounding_box": (x1, y1, x2, y2)
        })

    return cropped_signs

if __name__ == "__main__":
    print("")

