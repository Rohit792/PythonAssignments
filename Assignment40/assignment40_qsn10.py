"""
Question 10:
Train model with:
• max_depth = None
Calculate:
• Training accuracy
• Testing accuracy
If training accuracy is 100% but testing accuracy is lower, explain why this happens.


"""
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def displayInformation(message):
    border = "-"*40
    print(border)
    print(message)
    print(border)
 

def comaparePerformace():
    displayInformation("Train model with: max_depth = None")

    dataSet = pd.read_csv("student_performance_ml.csv")
        
    dataSet['PerformanceIndex'] = (dataSet['StudyHours'] * 2) + dataSet['Attendance']

    x = dataSet.drop("FinalResult", axis= 1)
    y = dataSet[["FinalResult"]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

    model = DecisionTreeClassifier(criterion="gini", max_depth= None, random_state= 42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_pred, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
 

def main():
    comaparePerformace()

if __name__ == "__main__":
    main()