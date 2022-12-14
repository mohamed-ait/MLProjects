# -*- coding: utf-8 -*-
"""Rock vs Mine Prediction .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-soE3xfJJngubh-R7eXBysBPj38Sa43E

importing the dependencies :
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

""" Data collection and Data Processing 
 
"""

# Loading the dataset to a pandas Dataframe :
sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header=None)

sonar_data.head()

# number of rows and columns :
sonar_data.shape

# describe statistical mesures of the data :
sonar_data.describe()

# counts diffrents values of a specific row :
sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#Separating data and labels :
X = sonar_data.drop(columns=60,axis=1)
Y= sonar_data[60]

X

Y

"""Training and test data 

"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

X_train

X_test

"""Model Training --------* Logistic Regression :"""

model =LogisticRegression()

# training the logistic regression  model with training data :
model.fit(X_train, Y_train)

# Accuracy on training data :

X_train_prediction = model.predict(X_train)

training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print(' the accuracy on training data is ', training_data_accuracy)

# Accuracy on test data :
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print(' the accuracy on test data is ', test_data_accuracy)

"""Making a predictive system : """

input_data = (0.0388,0.0324,0.0688,0.0898,0.1267,0.1515,0.2134,0.2613,0.2832,0.2718,0.3645,0.3934,0.3843,0.4677,0.5364,0.4823,0.4835,0.5862,0.7579,0.6997,0.6918,0.8633,0.9107,0.9346,0.7884,0.8585,0.9261,0.7080,0.5779,0.5215,0.4505,0.3129,0.1448,0.1046,0.1820,0.1519,0.1017,0.1438,0.1986,0.2039,0.2778,0.2879,0.1331,0.1140,0.1310,0.1433,0.0624,0.0100,0.0098,0.0131,0.0152,0.0255,0.0071,0.0263,0.0079,0.0111,0.0107,0.0068,0.0097,0.0067)

# changing the input_date to a numpy array : 
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance :
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)

if (prediction[0] == 'R') :
   print("the object is a Rock  ")
else : 
  print('the object is a Mine ')