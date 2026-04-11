"""
Question 4: 
Create a new DataFrame with details of 5 new students.
Use the trained model to predict their results.
Display predictions clearly.

Otput:
python assignment40_qsn4.py
Model Sucessfully Loaded
DecisionTreeClassifier(max_depth=5, random_state=42)
----------------------------------------
Step 1: Load Data set: 
----------------------------------------
   StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours
0           6          70             65                     8           4
1           4          90             40                     3           9
2           2          80             75                     9          10
3          15          60             80                     4          12
4           7          65             75                     6           5
----------------------------------------
Step 2: Data Analysis (EDS)
----------------------------------------
Shape of dataset:  (5, 5)
Colunm Name:  ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']

Prediction: [0 1 1 0 0]


"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
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
    print("Model Sucessfully Loaded")
    print(loaded_model)
    return loaded_model


#Step 2: Data Analysis (EDS) 
def analysis(df):
    displayInformation("Step 2: Data Analysis (EDS)")

    print("Shape of dataset: ", df.shape)
    print("Colunm Name: ", list(df.columns))
    print("Corelation: \n", df.corr())
    
#Step 3: Predict the result
def predictDataFrom(model, dataSet):
    predictions = model.predict(dataSet)  

    dataSet['Prediction'] = predictions
    print(f"\nPrediction: {predictions}")
    print("Dataset:\n", dataSet)
    


def main():
    model = LoadPreservedModel(fileName= "student.pkl")
    df = loadDataSet("student.json")
    analysis(df)
    predictDataFrom(model, df)
if __name__ == "__main__":
    main()