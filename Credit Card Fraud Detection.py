# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jtqd2VJz2ronlCqPfeaaLKybQnbxl9iP?usp=sharing

# **Credit Card Fraud Detection**

#**Objective** : To develop a machine learning project on Credit Card Fraud Detection.

#**Data Source** : https://www.kaggle.com/mlg-ulb/creditcardfraud

#**Import Library**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/creditcard.csv')

"""#**Describe Data**


"""

df.head()

df.tail()

df.info()

df.isnull().sum()

df.isnull().values.any()

df["Amount"].describe()

Genuine = len(df[df.Class == 0])
Fraud = len(df[df.Class == 1])
Genuine_percent = (Genuine / (Fraud + Genuine)) * 100
Fraud_percent = (Fraud / (Fraud + Genuine)) * 100

print("Number of Genuine transactions: ", Genuine)
print("Number of Fraud transactions: ", Fraud)
print("Percentage of Genuine transactions: {:.5f}".format(Genuine_percent))
print("Percentage of Fraud transactions: {:.5f}".format(Fraud_percent))

"""#**Data Visualization**

"""

labels = ["Genuine", "Fraud"]
fig, ax = plt.subplots()
count_classes = df.value_counts(df['Class'], sort = True)
ax.bar(labels, count_classes, width = 0.35)
ax.set_title("Visualization of Labels using Bar Graph")
ax.set_ylabel("Count")
print(count_classes)

labels = ["Genuine", "Fraud"]
fig, ax = plt.subplots()
count_classes = df.value_counts(df['Class'], sort = True)
ax.pie(count_classes, labels = labels, autopct = '%1.3f%%')
ax.set_title("Visualization of Labels using Pie Graph")
ax.legend();

"""## **Data Preprocessing**"""

# Perform Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df["NormalizedAmount"] = scaler.fit_transform(df["Amount"].values.reshape(-1, 1))
df.drop(["Amount", "Time"], inplace= True, axis= 1)

"""## **Define Target Variable (y) and Feature Variables (X)**"""

df.columns

#X = df[['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']]
X = df.drop(["Class"], axis = 1)
y = df["Class"]

"""# **Train Test Split**"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7, random_state = 252)
print("Shape of train_X: ", X_train.shape)
print("Shape of test_X: ", X_test.shape)

"""#**Modeling**"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree

#Logistic Regression
model = LogisticRegression()

#Decision Tree
model1 = DecisionTreeClassifier()

# Random Forest
model2 = RandomForestClassifier(n_estimators= 100)

"""#**Model Evaluation**"""

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
logistic_regression_score = model.score(X_test, y_test)

model1.fit(X_train, y_train)
y1_pred = model1.predict(X_test)
decision_tree_score = model1.score(X_test, y_test)

model2.fit(X_train, y_train)
y2_pred = model2.predict(X_test)
random_forest_score = model2.score(X_test, y_test)

"""#**Prediction**"""

print("Logistic Regression Score: ", logistic_regression_score)
print("Decision Tree Score: ", decision_tree_score)
print("Random Forest Score: ", random_forest_score)

y_pred
from sklearn.metrics import confusion_matrix, classification_report
confusion_matrix(y_test, y_pred)
print("Logistic Regression:\n\n", classification_report(y_test, y_pred))

y1_pred
from sklearn.metrics import confusion_matrix, classification_report
confusion_matrix(y_test, y1_pred)
print("Decision Tree:\n\n", classification_report(y_test, y1_pred))

fig, ax = plt.subplots(figsize=(80, 100))
plot_tree(model1, fontsize = 15);

y2_pred
from sklearn.metrics import confusion_matrix, classification_report
confusion_matrix(y_test, y2_pred)
print("Random Forest:\n\n", classification_report(y_test, y2_pred))

"""#**Explaination** :
The main motive of this project is to detect the credit card fraud transactions. The first step would be importing libraries that are numpy,  pandas, matplotlib then we would need to read our dataset and describing the data present in the dataset. Ater describing the data we would need to check that is their and null values in the dataset and handle it properly. After handling the null values we would need to do data visualization that is we would need to repersent data present in dataset in the form of graphs or charts. 

Then we would need to define target variable y and Feature variable X. Know we would to split data arrays into two subsets for training and testing the data.
"""
