# main.py
# Main script for running the Flask server
# Must be ran before running React app

from flask import Flask, jsonify, request
import numpy as np
from PIL import Image
import base64
from io import BytesIO
import descriptions
import tensorflow as tf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cnn_model = tf.keras.models.load_model("models/final_model.keras")

# Predict route - accepts POST requests with image and predicts the class
@app.route("/predict", methods=["POST"])
def predict():
    # Get image from request
    image_file = request.files['image']

    # Open image
    img = Image.open(image_file)
    img = img.convert('RGB')

    # Normalisation
    img = img.resize((32, 32))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  #add batch dimension

    # Prediction
    prediction = cnn_model.predict(img_array)
    predicted_label = np.argmax(prediction)

    predicted_label = int(predicted_label)  #convert to int
    description = descriptions.get_description(predicted_label)  #get description

    # Convert image to base64 for sending as JSON
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Send prediction result and image in base64
    return jsonify({
        "image": img_str,
        "predicted_label": predicted_label,
        "description": description
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)  #port 5001, avoids conflict with LibreTranslate
