# -*- coding: utf-8 -*-
"""Slary_data_model_with_linear_reg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hzW7nYif8Kwy-MbGDCZVZ1nqaeT2tSrd
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from lin_reg_model import Linear_Regression

#data collection and preprocessing
salary_data = pd.read_csv('/content/salary_data.csv')
salary_data.head()
salary_data.shape
#checking missing value
salary_data.isnull().sum()
#seperating the datasets
x = salary_data.drop(['Salary'], axis=1)
y = salary_data['Salary']
print(x)
print(y)

#spliting the train and Test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=2)
print(x.shape, x_train.shape, x_test.shape)

#training linear regression model
model = Linear_Regression(learning_rate=0.02, no_of_iterations=1000)      
model.fit(x_train, y_train)
#printing the parameters (weight and bias) values
print('weight= ',model.w[0])
print('bias= ',model.b)

test_data_prediction = model.predict(x_test)
print(test_data_prediction)

#find accuracy score using visualization tech
plt.scatter(x_test, y_test,color='red')
plt.plot(x_test, test_data_prediction, color='blue')
plt.xlabel('Work Experience')
plt.ylabel('Salary')
plt.show()

