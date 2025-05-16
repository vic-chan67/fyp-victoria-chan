# main.py
# Main script for running the Flask server
# Must be ran before running React app

import numpy as np
import base64
import tempfile
import os
import descriptions
import tensorflow as tf
from flask import Flask, jsonify, request
from PIL import Image
from io import BytesIO
from flask_cors import CORS
from full_pipeline import run_pipeline

app = Flask(__name__)
CORS(app)

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CNN_MODEL_PATH = os.path.join(BASE_DIR, "models", "final_cnn.keras")

cnn_model = tf.keras.models.load_model(CNN_MODEL_PATH)

# Pipeline route - accepts POST requests with image and runs the full pipeline
@app.route("/pipeline", methods=["POST"])
def pipeline():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        
        image_file = request.files['image']  #get image from request
        lang = request.args.get('lang', 'en')  #English default

        temp_path = os.path.join("temp_image.jpg")  #temporary path for saving image
        image_file.save(temp_path)

        results = run_pipeline(temp_path, lang)  #run pipeline
        return jsonify({"results": results}), 200  # return results
    
    except Exception as e:  #catch any exceptions
        print(f"Error in pipeline: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)  #port 5001, avoids conflict with LibreTranslate
