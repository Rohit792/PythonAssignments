"""
Question 7:
Train model using:
• random_state = 0
• random_state = 10
• random_state = 42
Compare testing accuracy.
Does the result change?


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
 
 

def checkRandonStateValues(randomStateValues):
    dataSet = pd.read_csv("student_performance_ml.csv")
    
    x = dataSet.drop("FinalResult", axis= 1)
    y = dataSet[["FinalResult"]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

    for i in range(len(randomStateValues)):
        model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= randomStateValues[i])
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_pred, y_test)
        print(f"Accuracy with Random state {randomStateValues[i]} is: {accuracy * 100}%")

def main():
   checkRandonStateValues([0, 10, 42])

if __name__ == "__main__":
    main()