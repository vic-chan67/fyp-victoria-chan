# testing.py
# Used to test trained model on test data, not used in main pipeline

import load_data
import descriptions
import translate
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
cnn_model = tf.keras.models.load_model("py-files/models/final_model.keras")

# Make predictions
print("\n---------- Making predictions ----------\n")
predictions = cnn_model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)  #get class with highest probability

# Print predictions
for i in range(10):  #display first 10 predictions
    predicted_label = predicted_classes[i]
    meaning = descriptions.get_description(predicted_label)
    print(f"Image {i + 1}: predicted class {predicted_label} = {meaning}")

# Ask user for target language
print("\n---------- Translation testing ----------\n")
print("Language codes (full list in \"lang_codes.txt\"): fr (French), es (Spanish), de (German)")
target_language = input("Enter target language code: ")

# Translate descriptions
translated_descriptions = []  #list for translated descriptions
for i in range(10):  #display first 10 translations
    predicted_label = predicted_classes[i]
    meaning = descriptions.get_description(predicted_label)  #get description from dictionary
    translation = translate.translate_text(meaning, target_language)  #translate description
    print(f"Image {i + 1}: {translation}")
    translated_descriptions.append(translation)

# # Display test images with their TRANSLATED predictions
# plt.figure(figsize=(5, 7))  #vertical layout
# plt.suptitle("Images with translated descriptions", fontsize=14, fontweight="bold")  #main title
# for i in range(5):
#     plt.subplot(5, 1, i + 1)
#     plt.imshow(X_test[i])
#     plt.axis("off")
#     predicted_label = predicted_classes[i]
#     desc = translated_desc[i]  #translated description
#     # desc = descriptions.get_description(predicted_label)  #dictionary description
#     plt.title(desc)
# plt.tight_layout()  #prevent graph overlap
# plt.show()

# Display test images with descriptions (both English and translated)
plt.figure(figsize=(13, 7))  #vertical layout
for i in range(5):
    # Left column
    plt.subplot(5, 2, 2 * i + 1)
    plt.imshow(X_test[i])
    plt.axis("off")
    predicted_label = predicted_classes[i]
    original_desc = descriptions.get_description(predicted_label)  #english desc
    plt.title(original_desc, fontsize=10)

    # Right column
    plt.subplot(5, 2, 2 * i + 2)
    plt.imshow(X_test[i])
    plt.axis("off")
    translated_desc = translated_descriptions[i]  #translated desc
    plt.title(translated_desc, fontsize=10)
plt.subplots_adjust(left=0.15, right=0.85, wspace=0.4, hspace=0.5)  #adjust layout
# plt.tight_layout(rect=[0, 0, 1, 1])  #prevent graph overlap
plt.show()