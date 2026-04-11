"""
Question 4: 
Without using accuracy_score, manually calculate accuracy:
Verify whether it matches sklearn accuracy.
 
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

def loadDataSet(fileName):
    df = pd.read_json(fileName)
    displayInformation("Step 1: Load Data set: ")
    print(df.head())
    return df

#Step 1: Laad Preserved model
def LoadPreservedModel(fileName):
    loaded_model = joblib.load(fileName)
    print("Trianed Model Sucessfully Loaded")
    print(loaded_model)
    return loaded_model


#Step 2: Data Analysis (EDS) 
def analysis(df):
    displayInformation("Step 2: Data Analysis (EDS)")

    print("Shape of dataset: ", df.shape)
    print("Colunm Name: ", list(df.columns))

#Step 3: Predict the result
def predictDataFrom(model, dataSet):
    predictions = model.predict(dataSet)  
    dataSet['Prediction'] = predictions
    print(f"\nPrediction: {predictions}")
    print("Dataset:\n", dataSet)
   

def calculate_accuracy_x(df):
    dataSet = pd.read_csv("student_performance_ml.csv")
    
    x = dataSet.drop("FinalResult", axis= 1)
    y = dataSet[["FinalResult"]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

    model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= 42)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    displayInformation("Calculate accuracy manually")
    y_test_new = y_test["FinalResult"].values
    totalMatched = sum(y_pred == y_test_new)

    final_manual_accuracy = totalMatched / len(y_test)
    print("Manually calculated accurancy: ", final_manual_accuracy)

    trained_y_pred = model.predict(df.drop("Prediction", axis= 1))
    print("Actual trinaed values: ", trained_y_pred)
    print("Values from trained model: ", df["Prediction"].values)
    trained_model_accuracy = accuracy_score(y_test_new, y_pred)
    print("Trained model accuracy: ", trained_model_accuracy)

    if final_manual_accuracy == trained_model_accuracy:
        print("Manual Accuary is matched with Tranined Model Accurany")
    else:
        print("Accuracy does not matched.")

def main():
    model = LoadPreservedModel(fileName= "student.pkl")
    df = loadDataSet("student.json")
    analysis(df)
    predictDataFrom(model, df)
    calculate_accuracy_x(df)

if __name__ == "__main__":
    main()