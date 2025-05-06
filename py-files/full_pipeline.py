# full_pipeline.py
# Full pipeline for detecting, cropping, classifying, and translating road signs

import tensorflow as tf
import numpy as np
import cv2
import time

from detection import detect_signs
from cropping import crop_signs
from descriptions import get_description
from translate import translate_text

# Preprocess cropped images (for CNN model)
def preprocess(img):
    resized = cv2.resize(img, (32, 32))
    normalised = resized / 255.0
    input_image = np.expand_dims(normalised, axis=0)
    return input_image

#---

# User language selection
#lang = input("Enter target language code (fr, es, de)/(full list in \"lang_codes.txt\"): ").strip().lower()
lang = "fr"

# Load model
cnn_model = tf.keras.models.load_model("py-files/models/final_model.keras")

start_time = time.time()

# Image path
image_path = "datasets/gtsdb-yolo/images/val/00788.jpg"

# Detection
image, bboxes = detect_signs(image_path)

# Cropping
cropped_signs = crop_signs(image, bboxes)

# Prediction
print("\n---------- PREDICTIONS AND TRANSLATIONS ----------")
for idx, sign in enumerate(cropped_signs):
    img = sign["image"]
    input_img = preprocess(img)
    prediction = cnn_model.predict(input_img)
    predicted_class = int(np.argmax(prediction))
    label = get_description(predicted_class)
    translation = translate_text(label, lang)
    print(f"Sign {idx + 1}: predicted class {predicted_class} = {label}, translated = {translation}")

end_time = time.time()

print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")