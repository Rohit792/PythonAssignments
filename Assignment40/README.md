# Python Assignment 40

## Machine Learning - Student Performance Prediction

---

## Dataset Description - Student Performance ML

The dataset `student_performance_ml.csv` contains academic and behavioral information of students. The objective of this dataset is to predict whether a student will **Pass (1)** or **Fail (0)** based on various input features.

Each row in the dataset represents one student, and each column represents a measurable factor that may influence academic performance.

### Features Description

- **StudyHours** - Number of hours a student studies per day.
- **Attendance** - Percentage of class attendance.
- **PreviousScore** - Marks obtained in the previous examination.
- **AssignmentsCompleted** - Number of assignments completed by the student.
- **SleepHours** - Average number of hours the student sleeps per day.
- **FinalResult** - Target variable (Output):
  - `1` → Pass
  - `0` → Fail

### Objective of the Dataset

The goal is to:
- Analyze how different factors affect student performance.
- Build a Machine Learning model to predict whether a student will pass or fail.
- Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model evaluation.

---

## Questions and Outputs

### Question 1: Feature Importance Analysis

After training the Decision Tree model, use `model.feature_importances_` to:
- Display importance score of each feature.
- Which feature contributes the most in predicting FinalResult?
- Which feature contributes the least?

### Question 2: Impact of Removing SleepHours

Remove the column `SleepHours` from the dataset:
- Train the model again.
- Compare new accuracy with previous accuracy.
- Does removing this feature affect performance?

### Question 3: Training with Limited Features

Train the model using only:
- StudyHours
- Attendance

Compare the accuracy with the full-feature model. Is the model still performing well?

---

### Output for Questions 1-3:

```bash
python assignment40_prg1.py
```

```
----------------------------------------
Step 1: Load Data set:
----------------------------------------
   StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
0         2.0          65             45                     3           5            0
1         3.0          70             50                     4           6            0
2         4.0          75             55                     5           6            0
3         5.0          80             60                     6           7            1
4         6.0          85             65                     7           7            1

----------------------------------------
Step 2: Data Analysis (EDS)
----------------------------------------
Shape of dataset:  (30, 6)
Colunm Name:  ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours', 'FinalResult']

----------------------------------------
 Step 3: Decide independent and Dependent variables
----------------------------------------

Features:
   StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours
0         2.0          65             45                     3           5
1         3.0          70             50                     4           6
2         4.0          75             55                     5           6
3         5.0          80             60                     6           7
4         6.0          85             65                     7           7

Labels:
0    0
1    0
2    0
3    1
4    1
Name: FinalResult, dtype: int64
Shape of x:  (30, 5)
Shape of y:  (30,)

----------------------------------------
Step5: Split the Data set for training and testing
----------------------------------------
Model Sucessfully created:  DecisionTreeClassifier(max_depth=5, random_state=42)

----------------------------------------
Step 6: Train the model
----------------------------------------
Model traning complted
Model Preserved sucessfully with Name:  student.pkl

----------------------------------------
Step 7: Evaluate the model
----------------------------------------
Model Evaluation Testing completed
(6,)
Expected output
27    1
15    0
23    0
17    0
8     0
9     0
Name: FinalResult, dtype: int64
Predicted output
[1 0 0 0 0 0]

----------------------------------------
Step 8: Evaluate the model Performance
----------------------------------------
Accuracy of model is:  100.0
Confusion Matrix:
[[5 0]
 [0 1]]
Classification Report
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         5
           1       1.00      1.00      1.00         1

    accuracy                           1.00         6
   macro avg       1.00      1.00      1.00         6
weighted avg       1.00      1.00      1.00         6

----------------------------------------
Step 9: Check model accuracy:
----------------------------------------
Trainign Accuracy:  100.0
Testing Accuracy:  100.0
Difference: 0.00%

----------------------------------------
Analysis on data
----------------------------------------
Good fit: Model generalises well
Impotance of features:  [0. 1. 0. 0. 0.]

___________________________________________________

----------------------------------------
1. After training the Decision Tree model:
----------------------------------------
Features Importance Ranking:
----------------------------------------
Attendance: 1.0
StudyHours: 0.0
PreviousScore: 0.0
AssignmentsCompleted: 0.0
SleepHours: 0.0
Most Important feature:  Attendance
Least Important feature:  SleepHours

----------------------------------------
2. Remove the column SleepHours from the dataset
----------------------------------------

Updated Features:
   StudyHours  Attendance  PreviousScore  AssignmentsCompleted
0         2.0          65             45                     3
1         3.0          70             50                     4
2         4.0          75             55                     5
3         5.0          80             60                     6
4         6.0          85             65                     7

Labels:
0    0
1    0
2    0
3    1
4    1
Name: FinalResult, dtype: int64
Shape of x:  (30, 4)
Shape of y:  (30,)
New Model Sucessfully created:  DecisionTreeClassifier(max_depth=5, random_state=42)

----------------------------------------
3. Trained the model again
----------------------------------------
New Model traning complted

----------------------------------------
Step: Evaluate the model
----------------------------------------
Model Evaluation Testing completed
(6,)
Expected output
27    1
15    0
23    0
17    0
8     0
9     0
Name: FinalResult, dtype: int64
Predicted output
[1 0 0 0 0 0]

----------------------------------------
Step 8: Evaluate the model Performance
----------------------------------------
Accuracy of new model is:  100.0
Old Accuracy : 1.0
New Accuracy:  1.0

----------------------------------------
3. Train the model using only with SleepHours and FinalResult
----------------------------------------

Updated Features:
   SleepHours
0           5
1           6
2           6
3           7
4           7

Labels:
0    0
1    0
2    0
3    1
4    1
Name: FinalResult, dtype: int64
Shape of x:  (30, 1)
Shape of y:  (30,)
New Model Sucessfully created:  DecisionTreeClassifier(max_depth=5, random_state=42)

New Model traning complted

----------------------------------------
Step: Evaluate the model
----------------------------------------
Prediction of new model is:  [1 0 0 0 0 0]
Test accuracy with new model is:  1.0
```

---

### Question 4: Predicting New Students

Create a new DataFrame with details of 5 new students. Use the trained model to predict their results. Display predictions clearly.

**Output:**

```bash
python assignment40_qsn4.py
```

```
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
Dataset:
    StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  Prediction
0           6          70             65                     8           4           0
1           4          90             40                     3           9           1
2           2          80             75                     9          10           1
3          15          60             80                     4          12           0
4           7          65             75                     6           5           0
```

---

### Question 5: Manual Accuracy Calculation

Without using `accuracy_score`, manually calculate accuracy and verify whether it matches sklearn accuracy.

**Output:**

```
Trianed Model Sucessfully Loaded
DecisionTreeClassifier(max_depth=5, random_state=42)

----------------------------------------
Step 1: Load Data set:
----------------------------------------
   StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours
0           6          70             65                     8           4
1           1          80             30                     0          10
2           2          80             75                     9          10
3          15          60             80                     4          12
4           7          65             75                     6           5

----------------------------------------
Step 2: Data Analysis (EDS)
----------------------------------------
Shape of dataset:  (5, 5)
Colunm Name:  ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']

Prediction: [0 1 1 0 0]
Dataset:
    StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  Prediction
0           6          70             65                     8           4           0
1           1          80             30                     0          10           1
2           2          80             75                     9          10           1
3          15          60             80                     4          12           0
4           7          65             75                     6           5           0

----------------------------------------
Calculate accuracy manually
----------------------------------------
Manually calculated accurancy:  1.0
Actual trinaed values:  [0 1 1 0 0]
Values from trained model:  [0 1 1 0 0]
Trained model accuracy:  1.0
Manual Accuary is matched with Tranined Model Accurany
```

---

### Question 6: Misclassified Students

Identify students where `y_test != y_pred`:
- Display those rows.
- How many students were misclassified?
- What common pattern do you observe?

**Output:**

```
Y_Pred:  [1 0 0 0 0 0]
y_test:  [1 0 0 0 0 0]
Miss classified students are:  0
```

---

### Question 7: Impact of random_state

Train model using different `random_state` values:
- random_state = 0
- random_state = 10
- random_state = 42

Compare testing accuracy. Does the result change?

**Output:**

```
Accuracy with Random state 0 is: 100.0%
Accuracy with Random state 10 is: 100.0%
Accuracy with Random state 42 is: 100.0%
```

---

### Question 8: Decision Tree Visualization

Use:
```python
from sklearn.tree import plot_tree
```

Visualize the trained decision tree:
- Which feature appears at the root node?
- Why do you think that feature was selected first?

**Output:**

```
Model Accuracy: 100.00%

----------------------------------------
Decision Tree Visualization
----------------------------------------
Root node feature: Attendance

Why 'Attendance' was selected first:
This feature provides the highest Gini impurity reduction,
meaning it best separates Pass/Fail students at the first split.
```

---

### Question 9: Adding Performance Index Feature

Create a new column:
```
PerformanceIndex = (StudyHours * 2) + Attendance
```

Train the model including this new feature. Does accuracy improve?

**Output:**

```
Model Accuracy: 100.00%

----------------------------------------
Decision Tree Visualization
----------------------------------------
Root node feature: StudyHours

Why 'StudyHours' was selected first:
This feature provides the highest Gini impurity reduction,
meaning it best separates Pass/Fail students at the first split.

Previously Feature importance was: Attendance
Now Feature importance is:  StudyHours
```

---

### Question 10: Training with max_depth = None

Train model with `max_depth = None`.

Calculate:
- Training accuracy
- Testing accuracy

If training accuracy is 100% but testing accuracy is lower, explain why this happens.

**Output:**

```
----------------------------------------
Train model with: max_depth = None
----------------------------------------
Model Accuracy: 100.00%
```

---

## Summary

This assignment demonstrates:
- Feature importance analysis using Decision Trees
- Impact of feature removal on model performance
- Manual accuracy calculation and verification
- Model visualization and interpretation
- Feature engineering with Performance Index
- Understanding of model parameters like `random_state` and `max_depth`
