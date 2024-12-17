import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

def load_and_preprocess_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
    
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    x_train = x_train.reshape((-1, 28, 28, 1))
    x_test = x_test.reshape((-1, 28, 28, 1))
    
    return x_train, y_train, x_test, y_test

def create_model():
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(10, activation='softmax')  
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model

def train_model(x_train, y_train, x_test, y_test):
    model = create_model()
    
    
    early_stopping = EarlyStopping(
        monitor='val_loss',     
        patience=5,
        restore_best_weights=True  
    )
    
    history = model.fit(
        x_train, y_train,
        epochs=20, 
        batch_size=64,
        validation_split=0.2,
        verbose=1,
        callbacks=[early_stopping]  
    )
   
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"\nTest accuracy: {test_accuracy:.4f}")
   
    return model, history

def predict_and_save(model, x_test_external):
    x_test_preprocessed = x_test_external.astype('float32') / 255.0
    x_test_preprocessed = x_test_preprocessed.reshape((-1, 28, 28, 1))
    
    predictions = model.predict(x_test_preprocessed)
    
    y_test_pred = np.argmax(predictions, axis=1)
    
    np.save('y_test.npy', y_test_pred)
    
    return y_test_pred

def visualize_training_history(history):
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='lower right')

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper right')
    
    plt.tight_layout()
    plt.show()

def main():
    x_train, y_train, x_test, y_test = load_and_preprocess_data()
    
    model, history = train_model(x_train, y_train, x_test, y_test)
    
    visualize_training_history(history)
    
    x_test_external = np.load('Data/fashion_x_test.npy')
    
    predictions = predict_and_save(model, x_test_external)
    
    print("Predictions saved to 'y_test.npy'")

if __name__ == '__main__':
    main()