# training.py
# Train CNN model on GTRSB dataset

import load_data
import model
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping # type: ignore
import matplotlib.pyplot as plt

# Load dataset
print("---------- Loading dataset ----------")
X_train, y_train = load_data.load_training_data()
X_test, y_test = load_data.load_testing_data()

# Build CNN model
print("\n---------- Building model ----------")
cnn_model = model.build_model()

# Callbacks for model training
checkpoint = ModelCheckpoint("models/best_model.keras", save_best_only=True, monitor="val_loss", mode="min")  #only save best model
early_stopping = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)  #stop training if no improvement after 5 epochs

# Train model
print("\n---------- Training model ----------")
history = cnn_model.fit(
    X_train, y_train,
    epochs=15,
    batch_size=128,
    validation_data=(X_test, y_test),
    callbacks=[checkpoint, early_stopping]
)

# Save model
cnn_model.save("models/final_model.keras")
print("Model trained and saved")

# Plot training & validation accuracy values
plt.figure(figsize=(12, 5))

# Accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)

# Loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()