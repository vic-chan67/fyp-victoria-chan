import os
import numpy as np
import pandas as pd
import cv2
from tensorflow.keras.utils import to_categorical

# Data paths
train_folder = "data/Train"
test_folder = "data/Test"
train_csv = "data/Train.csv"
test_csv = "data/Test.csv"

# Image size
img_size = (32, 32)

# Load training data
def load_training_data():
    images = []
    labels = []

    # Load training data from CSV
    # Only load ClassID and Path columns
    df = pd.read_csv(train_csv, usecols=["ClassId", "Path"])

    for i, row in df.iterrows():
        # Get filename from Path column
        img_path = os.path.join(os.path.dirname(train_csv), row["Path"].strip())

        img = cv2.imread(img_path)  #load img
        img = cv2.resize(img, img_size)  #resize img

        images.append(img)
        labels.append(row["ClassId"])
    
    # Convert lists to NumPy arrays
    images = np.array(images, dtype=np.float32) / 255.0  #normalisation
    labels = to_categorical(labels, 43)  #one-hot encoding

    return images, labels

# Load testing data
def load_testing_data():
    images = []
    labels = []

    # Load test data from CSV (use only ClassId and Path columns)
    df = pd.read_csv(test_csv, usecols=["ClassId", "Path"])

    for i, row in df.iterrows():
        # Get filename from Path column
        img_path = os.path.join(test_folder, os.path.basename(row["Path"]).strip())

        img = cv2.imread(img_path)  #load img
        img = cv2.resize(img, img_size)  #resize img

        images.append(img)
        labels.append(row["ClassId"])

    images = np.array(images, dtype=np.float32) / 255.0  #normalisation
    labels = to_categorical(labels, 43)  #one-hot encoding

    return images, labels

# Test
if __name__ == "__main__":
    X_train, y_train = load_training_data()
    print(f"Training Data Loaded: {X_train.shape[0]} samples")

    X_test, y_test = load_testing_data()
    print(f"Testing Data Loaded: {X_test.shape[0]} samples")