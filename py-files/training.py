# training.py
# Train CNN model on GTRSB dataset

import load_data
import model
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping # type: ignore

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