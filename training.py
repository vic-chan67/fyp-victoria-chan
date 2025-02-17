import load_data  # Import dataset loading functions
import model  # Import CNN model definition
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

# Load dataset
print("Loading dataset...")
X_train, y_train = load_data.load_training_data()
X_test, y_test = load_data.load_testing_data()

# Build the CNN model
print("Building model...")
cnn_model = model.build_model()

# Define callbacks for training
checkpoint = ModelCheckpoint("models/best_model.keras", save_best_only=True, monitor="val_loss", mode="min")
early_stopping = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)

# Train the model
print("Training model...")
history = cnn_model.fit(
    X_train, y_train,
    epochs=15,
    batch_size=32,
    validation_data=(X_test, y_test),
    callbacks=[checkpoint, early_stopping]
)

# Save final model
cnn_model.save("models/final_model.keras")
print("Model training complete. Model saved successfully!")
