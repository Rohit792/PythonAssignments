"""
Question:
Dataset Description - Student Performance ML
Dataset
The dataset student_performance_ml. csv contains academic and behavioral information of students. The objective of this dataset is to predict whether a student will Pass (1) or Fail (0) based on various input features.
Each row in the dataset represents one student, and each column represents a measurable factor that may influence academic performance.
Features Description
    • StudyHours - Number of hours a student studies per day.
    • Attendance - Percentage of class attendance.
    • PreviousScore - Marks obtained in the previous examination.
    • AssignmentsCompleted - Number of assignments completed by the student.
    • SleepHours - Average number of hours the student sleeps per day.
    • FinalResult - Target variable (Output):
        1 → Pass
        0 → Fail
Objective of the Dataset
The goal is to:
Analyze how different factors affect student performance.
    • Build a Machine Learning model to predict whether a student will pass or fail.
    • Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model evaluation.

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

#Step 1: Laad Dataset
def loadDataSet(fileName):
    df = pd.read_csv(fileName)
    displayInformation("Step 1: Load Data set: ")
    print(df.head(5))
    return df

#Step 2: Data Analysis (EDS) 
def analysis(df):
    displayInformation("Step 2: Data Analysis (EDS)")

    print("Shape of dataset: ", df.shape)
    print("Colunm Name: ", list(df.columns))

# Step 3: Decide independent and Dependent variables
def getDependantAndIndipendantVeriable(df):
    displayInformation(" Step 3: Decide independent and Dependent variables")

    x = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    print("\nFeatures: ")
    print(x.head(5))

    print("\nLabels: ")
    print(y.head(5))

    print("Shape of x: ", x.shape)
    print("Shape of y: ", y.shape)

def PreserveModel(model, fileName):
    joblib.dump(model, filename= fileName)
    print("Model Preserved sucessfully with Name: ", fileName)
    
#Step5: Split the Data set for training and testing
def modelTraning(df):

    x = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]
    print("\n")
    displayInformation("Step5: Split the Data set for training and testing")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

    model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= 42)

    print("Model Sucessfully created: ", model)
    print("\n")
    displayInformation("Step 6: Train the model")
    model.fit(x_train, y_train)
    print("Model traning complted")

    PreserveModel(model, "student.pkl")

    displayInformation("Step 7: Evaluate the model")
    Y_pred = model.predict(x_test)

    print("Model Evaluation Testing completed")
    print(Y_pred.shape)

    print("Expected output")
    print(y_test)

    print("Predicted output")
    print(Y_pred)

    displayInformation("Step 8: Evaluate the model Performance")
    test_accuracy = accuracy_score(y_test, Y_pred)
    print("Accuracy of model is: ", test_accuracy*100)

    cm = confusion_matrix(y_test, Y_pred)
    print("Confusion Matrix: ")
    print(cm)

    print("Classification Report")
    print(classification_report(y_test, Y_pred))

    displayInformation("Step 9: Check model accuracy:")
    y_train_pred = model.predict(x_train)
    traing_accuracy = accuracy_score(y_train, y_train_pred)

    print("Trainign Accuracy: ", traing_accuracy * 100)
    print("Testing Accuracy: ", test_accuracy * 100)
    print(f"Difference: {(traing_accuracy - test_accuracy) * 100:.2f}%")

    displayInformation("Analysis on data")
    modelPerformance = ""
    if traing_accuracy < 0.7 and test_accuracy < 0.7:
        print("Underfitting: Model is too simple")
        modelPerformance = "Underfitting: Model is too simple"
    elif traing_accuracy > 0.95 and (traing_accuracy - test_accuracy) > 0.1:
        print("Overfitting: Model is too complex")
        modelPerformance = "Overfitting: Model is too complex"
    else:
        print("Good fit: Model generalises well")
        modelPerformance = "Good fit: Model generalises well"


    print("Impotance of features: ", model.feature_importances_)
    featuresName = list(df.drop("FinalResult", axis=1).columns)
    importance = model.feature_importances_
    feature_importance_pairs = sorted(zip(featuresName, importance), key= lambda x: x[1], reverse= True)

    print("\n")
    print("___________________________________________________\n")
    displayInformation("1. After training the Decision Tree model:")
    print("Features Importance Ranking: ")
    print("-"*40)
    for features, importance in feature_importance_pairs:
        print(f"{features}: {importance}")
    print("Most Important feature: ", feature_importance_pairs[0][0])
    print("Least Important feature: ", feature_importance_pairs[-1][0])

    print("\n")
    displayInformation("2. Remove the column SleepHours from the dataset")
    x = df.drop(["SleepHours","FinalResult"], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)
    
    print("\nUpdated Features: ")
    print(x.head(5))

    print("\nLabels: ")
    print(y.head(5))

    print("Shape of x: ", x.shape)
    print("Shape of y: ", y.shape)
    model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= 42)

    print("New Model Sucessfully created: ", model)
    print("\n")
    displayInformation("3. Trained the model again")
    model.fit(x_train, y_train)
    print("New Model traning complted")
    
    displayInformation("Step: Evaluate the model")
    Y_pred_new = model.predict(x_test)

    print("Model Evaluation Testing completed")
    print(Y_pred_new.shape)

    print("Expected output")
    print(y_test)

    print("Predicted output")
    print(Y_pred_new)

    displayInformation("Step 8: Evaluate the model Performance")
    test_accuracy_new = accuracy_score(y_test, Y_pred_new)
    print("Accuracy of new model is: ", test_accuracy_new*100)

    print("Old Accuracy :", test_accuracy)
    print("New Accuracy: ", test_accuracy_new)



def onylWithStudyHoursAndAttendance(df):

    print("\n")
    displayInformation("3. Train the model using only with SleepHours and FinalResult")
    x = df[["SleepHours"]]
    y = df["FinalResult"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)
    
    print("\nUpdated Features: ")
    print(x.head(5))

    print("\nLabels: ")
    print(y.head(5))

    print("Shape of x: ", x.shape)
    print("Shape of y: ", y.shape)
    model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= 42)

    print("New Model Sucessfully created: ", model)
    print("\n")
    model.fit(x_train, y_train)
    print("New Model traning complted")
    
    displayInformation("Step: Evaluate the model")
    Y_pred_new = model.predict(x_test)
    print("Prediction of new model is: ", Y_pred_new)

    test_accuracy_new = accuracy_score(y_test, Y_pred_new)
    print("Test accuracy with new model is: ", test_accuracy_new)

def predictInteractiveUsing(model):
    displayInformation("Interactive Student Prediction")
    
    print("Enter student details:")
    study_hours = float(input("Study Hours per day: "))
    attendance = float(input("Attendance %: "))
    previous_score = float(input("Previous Score: "))
    assignments = int(input("Assignments Completed: "))
    sleep_hours = float(input("Sleep Hours per day: "))
    
    student_data = pd.DataFrame({
        'StudyHours': [study_hours],
        'Attendance': [attendance],
        'PreviousScore': [previous_score],
        'AssignmentsCompleted': [assignments],
        'SleepHours': [sleep_hours]
    })

    prediction = model.predict(student_data)
    
    print(f"\nPrediction: {'PASS' if prediction[0] == 1 else 'FAIL'}")

def StudentPerformance():

    df = loadDataSet("student_performance_ml.csv")
    analysis(df)
    getDependantAndIndipendantVeriable(df)
    modelTraning(df)
    onylWithStudyHoursAndAttendance(df)


def main():
    StudentPerformance()

if __name__ == "__main__":
    main()