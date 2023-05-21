# -*- coding: utf-8 -*-
"""
Created on Mon May 22 02:55:44 2023

@author: User
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 讀取CSV數據集
data = pd.read_csv('data.csv')

# 分割特徵和目標變數
X = data[['Humidity']]
y = data['Temperature']

# 分割訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立支持向量機回歸模型
model = SVR(kernel='linear')

# 訓練模型
model.fit(X_train, y_train)

# 使用測試集進行預測
y_pred = model.predict(X_test)

# 評估模型性能
mse = mean_squared_error(y_test, y_pred)
accuracy = 1 - mse / y_test.var()
print('模型準確度：', accuracy)

# 繪製散點圖和回歸直線
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.title('Linear Regression - Humidity vs Temperature')
plt.legend()
plt.show()
