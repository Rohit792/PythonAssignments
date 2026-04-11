"""
Question 6:

Identify students where:
y_ test != y_pred
• Display those rows.
• How many students were misclassified?
• What common pattern do you observe?
 
"""
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import joblib

def displayInformation(message):
    border = "-"*40
    print(border)
    print(message)
    print(border)
 
 

def defineMissClasifiedStudent():
    dataSet = pd.read_csv("student_performance_ml.csv")
    
    x = dataSet.drop("FinalResult", axis= 1)
    y = dataSet[["FinalResult"]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

    model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= 42)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print("Y_Pred: ", y_pred)
    print("y_test: ", y_test["FinalResult"].values)
    y_pred_values = y_test["FinalResult"].values

    missClasifiedStudent = []
    for i in range(len(y_pred_values)):
        if y_pred[i] != y_pred_values[i]:
            missClasifiedStudent.append(y_pred[i])
    print("Miss classified students are: ", len(missClasifiedStudent))

def main():
   defineMissClasifiedStudent()

if __name__ == "__main__":
    main()