# testing.py
# Test trained CNN model on test data

import load_data
import descriptions
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

# Load test data
print("---------- Loading test data ----------")
X_test, y_test = load_data.load_testing_data()

# Shuffle test data
X_test, y_test = shuffle(X_test, y_test, random_state=None)

# Load trained model
print("\n---------- Loading trained model ----------")
cnn_model = tf.keras.models.load_model("models/final_model.keras")

# Make predictions
print("\n---------- Making predictions ----------\n")
predictions = cnn_model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)  #get class with highest probability

# Print predictions
for i in range(10):  #display first 10 predictions
    predicted_label = predicted_classes[i]
    meaning = descriptions.get_description(predicted_label)
    print(f"Test Image {i + 1}: Predicted Class {predicted_label} = {meaning}")

# Display test images with their predictions
plt.figure(figsize=(5, 10))  #vertical layout
for i in range(5):
    plt.subplot(5, 1, i + 1)
    plt.imshow(X_test[i])
    plt.axis("off")
    predicted_label = predicted_classes[i]
    meaning = descriptions.get_description(predicted_label)
    plt.title(meaning)
plt.tight_layout()  #prevent graph overlap
plt.show()