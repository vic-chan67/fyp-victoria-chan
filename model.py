import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, Dropout

def build_model():

    model = Sequential([
        Input(shape=(32, 32, 3)),  #input layer 32x32 with 3 channels
        
        # First convolutional layer
        Conv2D(32, (3, 3), activation='relu'),  #32 filters, 3x3 kernel, relu activation for non-linearity
        MaxPooling2D(pool_size=(2, 2)),  #pooling layer to reduce spatial dimensions, prevent overfitting

        # Second convolutional layer
        Conv2D(64, (3, 3), activation='relu'),  #64 filters, 3x3 kernel, relu activation for non-linearity
        MaxPooling2D(pool_size=(2, 2)),  #pooling layer to reduce spatial dimensions, prevent overfitting

        Flatten(),  #flatten output to feed into dense layer

        # Fully connected dense layer
        Dense(128, activation='relu'),  #128 neurons, relu activation for non-linearity
        Dropout(0.5),  #dropout layer to prevent overfitting

        # Output layer with 43 classes
        # Softmax activation converting output to probabilities
        Dense(43, activation='softmax')
    ])

    model.compile(
        loss='categorical_crossentropy',  #loss function for multi-class classification
        optimizer='adam',  #adam optimiser to adjust weights
        metrics=['accuracy']  #accuracy metric to evaluate model
    )

    return model