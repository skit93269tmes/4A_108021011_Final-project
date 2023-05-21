# 4A_108021011_Final-project
# 4A Final project in  智慧物聯網。

# 組員：108021011 蘇邑洋 108021160 郭鍇勳



# 第一隻程式概述 Arduino_Finalproject.ino
# 第一隻程式是一個基於 Arduino 的 IoT 裝置程式，用於收集溫度和濕度數據並將其推送到 MQTT 代理伺服器上。

	# 程式功能
	1. 收集溫度和濕度數據、將數據推送到 MQTT 代理伺服器
	# 程式結構
	1. 引入必要的程式庫
	2. 定義 Wi-Fi 和 MQTT 相關訊息、定義 DHT11 溫濕度感應器的連接腳位和 LED 控制腳位、宣告全域變數和物件、定義 DHT11 感應器數據讀取函數、定義濕度控制函數、定義接收 MQTT 訊息的回調函數
	3. 初始化 Wi-Fi 連線和 MQTT 客戶端
	4. 設定主迴圈、如果 MQTT 客戶端未連線，重新連線
	5. 檢查是否到達發布數據的時間間隔
	6. 讀取溫濕度數據
	7. 執行濕度控制
	8. 發布數據到 MQTT 代理伺服器

# 第二隻程式概述 DAI.py
# 第二隻程式是一個基於 Arduino 的 IoT 裝置程式，用於收集溫度和濕度數據並將其推送到 MQTT 代理伺服器上。

# 套件：
      1. import time
      2. import random
      3. import requests
      4. import DAN
      5. import paho.mqtt.client as mqtt
      6. import csv

	# 程式功能
	1. 收集溫度和濕度數據
	2. 將數據推送到 MQTT 代理伺服器
	# 程式結構
	1. 引入必要的程式庫
	2. 定義 Wi-Fi 和 MQTT 相關訊息
	3. 定義 DHT11 溫濕度感應器的連接腳位和 LED 控制腳位
	4. 宣告全域變數和物件
	5. 定義 DHT11 感應器數據讀取函數
	6. 定義濕度控制函數、定義接收 MQTT 訊息的回調函數
	7. 初始化 Wi-Fi 連線和 MQTT 客戶端、設定主迴圈
	8. 如果 MQTT 客戶端未連線，重新連線、檢查是否到達發布數據的時間間隔、讀取溫濕度數據、執行濕度控制、發布數據到 MQTT 代理伺服器

# 第三隻程式概述 AI演算法SVM線性.py
# 第三隻程式是一個基於支持向量機回歸的溫度預測模型。該模型使用濕度作為特徵變數，預測溫度。

# 套件：
    1. import pandas as pd
    2. from sklearn.model_selection import train_test_split
    3. from sklearn.svm import SVR
    4. from sklearn.metrics import mean_squared_error
    5. import matplotlib.pyplot as plt

	# 程式功能、讀取 CSV 數據集、分割特徵和目標變數、分割訓練集和測試集
	1. 建立支持向量機回歸模型、訓練模型
	2. 使用測試集進行預測、評估模型性能
	3. 繪製散點圖和回歸直線、
	# 程式結構
	1. 引入必要的程式庫
	2. 讀取 CSV 數據集、分割特徵和目標變數、分割訓練集和測試集
	3. 建立支持向量機回歸模型、訓練模型
	4. 使用測試集進行預測、評估模型性能=、繪製散點圖和回歸直線


# 注意： 請確保在執行第三隻程式之前已經先執行第一隻程式和第二隻程式，以確保有可用的數據集。
