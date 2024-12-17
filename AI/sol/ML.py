import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import pandas as pd
X_train = pd.read_csv('./Data/housing_x_train.csv', sep=',', encoding='utf-8').values
y_train = pd.read_csv('./Data/housing_y_train.csv', sep=',', encoding='utf-8').values
X_test = pd.read_csv('./Data/housing_x_test.csv', sep=',', encoding='utf-8').values


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


import tensorflow as tf
from tensorflow.keras import layers
model = tf.keras.Sequential([
    layers.Dense(10, activation='relu', input_dim=X_train_scaled.shape[1]),
    layers.Dense(20, activation='relu'),  
    layers.Dense(10, activation='relu'),  
    layers.Dense(1) 
])
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, verbose=1)


import numpy as np
y_pred = model.predict(X_test_scaled)
np.savetxt('housing_y_test.csv', y_pred, delimiter=",", fmt="%g")