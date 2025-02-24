# -*- coding: utf-8 -*-
"""Copy of DiabAi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1prJszzgMWPdhUNkm6X3OV_SCEqeNhP-u
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

# Import dataset
Data = pd.read_csv('Dataset of Diabetes .csv')

# Display the first 5 rows of the dataset
print(Data.head())

# Split data into training set (x) and testing set (y)
x = Data.drop(columns=["ID", "No_Pation", "Gender", "CLASS"])  # Exclude non-numeric and non-target columns
y = Data["CLASS"]

# Map classes to binary values
y = y.map({'N': 0, 'Y': 1, 'P': 1})

# Handle non-finite values (NaN or inf)
y = y.fillna(0)  # Replace NaN with 0
y = y.replace([np.inf, -np.inf], 0)  # Replace inf with 0

# Display unique values in y
print("Unique values in y:", y.unique())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train_np = x_train.to_numpy()
y_train_np = y_train.astype('float32').to_numpy()  # Convert to float32

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(256, input_shape=(x_train.shape[1],), activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train_np, y_train_np, epochs=1000)

model.evaluate(x_test, y_test)