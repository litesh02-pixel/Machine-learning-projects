# -*- coding: utf-8 -*-
"""Project_4_gold_price_prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12KKDR5chN7wEPJ6pM1ew0G547JAiGdZJ

Using Random FOrest Regressor
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor

gold_data = pd.read_csv('/content/gld_price_data.csv')
gold_data.head()

gold_data.shape

gold_data.isnull().sum()

gold_data.describe()

gold_data.info()

correlation = gold_data.corr()

plt.figure(figsize=(8,8))

sns.heatmap(correlation, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size':8}, cmap='Blues')

print(correlation['GLD'])

#check distribution of gold price
sns.displot(gold_data['GLD'], color='green')

#sploting the feature and target column
x = gold_data.drop(['Date', 'GLD'], axis=1)
y = gold_data['GLD']
print(x)

print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
print(x.shape, x_train.shape, x_test.shape)

#Model training (RandomForest)
regressor = RandomForestRegressor()
regressor.fit(x_train, y_train)

#model evaluation
test_data_prediction = regressor.predict(x_test)
print(test_data_prediction)

#R_square error
error_score = metrics.r2_score(y_test, test_data_prediction)
print(error_score)

#compare the actual values & predicted values in plot
y_test = list(y_test)
plt.plot(y_test, color='red', label='Actual Value')
plt.plot(test_data_prediction, color='blue', label='Predicted Value')
plt.xlabel('No. of values')
plt.ylabel('Gold Price')
plt.title('Actual values vs Predicted values')
plt.legend()
plt.show()

