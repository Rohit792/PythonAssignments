"""
Question:
Dataset Description — Student Performance ML Dataset
The dataset student_performance_ml.csv contains academic and behavioral information of students. 
The objective of this dataset is to predict whether a student will Pass (1) or Fail (0) based on various input features.

Each row in the dataset represents one student, 
and each column represents a measurable factor that may influence academic performance.

Objective of the Dataset

The goal is to:
- Analyze how different factors affect student performance.
- Build a Machine Learning model to predict whether a student will pass or fail.
- Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model evaluation.

"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

def displayInformation(message):
    border = "-"*40
    print(border)
    print(message)
    print(border)

#Step 1: Laad Dataset
def loadDataSet(fileName):
    df = pd.read_csv(fileName)
    displayInformation("Step 1: Load Data set: ")
    print(df.head())
    return df

#Step 2: Data Analysis (EDS) 
def analysis(df):
    displayInformation("Step 2: Data Analysis (EDS)")

    print("Shape of dataset: ", df.shape)
    print("Colunm Name: ", list(df.columns))

    print("Missing values (per column)")
    print(df.isnull().sum())

    print("Statistical report of dataset")
    print(df.describe())


# Step 3: Decide independant and Dependant veriables
def getDependantAndIndipendantVeriable(df):
    displayInformation(" Step 3: Decide independant and Dependant veriables")

    x = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    print("\nFeatures: ")
    print(x.head())

    print("\nLabels: ")
    print(y.head())

    print("Shape of x: ", x.shape)
    print("Shape of y: ", y.shape)

    print("Missing values (per column)")
    print(df.isnull().sum())

#Step 4: Visualisation of dataset
def visualisation(df):
    displayInformation("Step 4: Visualisation of dataset")
    plt.figure(figsize=(7,5))

    for fResult in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == fResult]
        plt.scatter(temp[7,5])

#Step5: Split the Data set for training and testing
def modelTraning(df):

    x = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]
    displayInformation("Step5: Split the Data set for training and testing")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

    print("Shape of x_train: ", x_train.shape)
    print("Shape of x_test: ", x_test.shape)
    print("Shape of y_test: ", y_test.shape)
    print("Shape of y_train: ", y_train.shape)

    model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= 42)

    print("Model Sucessfully created: ", model)

    displayInformation("Step 6: Train the model")
    model.fit(x_train, y_train)
    print("Model traning complted")

    displayInformation("Step 7: Evaluate the model")
    Y_pred = model.predict(x_test)

    print("Model Evaluation Testing completed")
    print(Y_pred.shape)

    print("Expected output")
    print(y_test)

    print("Predicted output")
    print(Y_pred)

    displayInformation("Step 8: Evaluate the model Performance")
    accuracy = accuracy_score(y_test, Y_pred)
    print("Accuracy of model is: ", accuracy*100)

    cm = confusion_matrix(y_test, Y_pred)
    print("Confusion Matrics: ")
    print(cm)

    print("Classification Report")
    print(classification_report(y_test, Y_pred))

    displayInformation("Step 9: Plot confusion Matrix")
    data = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = model.classes_)
    data.plot()

    plt.title = "Confusion matrics of Student Performance data set"
    plt.show()

def StudentPerformance():

    df = loadDataSet("student_performance_ml.csv")
    print(df)
    analysis(df)
    getDependantAndIndipendantVeriable(df)
    modelTraning(df)
    

def main():
    StudentPerformance()

if __name__ == "__main__":
    main()