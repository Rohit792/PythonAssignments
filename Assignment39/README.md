# Python Assignment 39

## Python Programming - Machine Learning

---

### Dataset Description — Student Performance ML Dataset

The dataset `student_performance_ml.csv` contains academic and behavioral information of students. The objective of this dataset is to predict whether a student will **Pass (1)** or **Fail (0)** based on various input features.

Each row in the dataset represents one student, and each column represents a measurable factor that may influence academic performance.

### Features Description

| Feature                | Description                                          |
|------------------------|------------------------------------------------------|
| `StudyHours`           | Number of hours a student studies per day             |
| `Attendance`           | Percentage of class attendance                       |
| `PreviousScore`        | Marks obtained in the previous examination           |
| `AssignmentsCompleted` | Number of assignments completed by the student       |
| `SleepHours`           | Average number of hours the student sleeps per day   |
| `FinalResult`          | Target variable (Output): `1` → Pass, `0` → Fail    |

### Objective of the Dataset

The goal is to:

- Analyze how different factors affect student performance.
- Build a Machine Learning model to predict whether a student will pass or fail.
- Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model evaluation.

---

## Programs

### 1. Train a Decision Tree Model

Import `DecisionTreeClassifier` from `sklearn`. Create a model object and train it using `fit()`.

### 2. Predict and Compare Results

Use the trained model to predict results for `X_test`. Display predicted values along with actual values.

### 3. Calculate Model Accuracy

Calculate model accuracy using `accuracy_score`. Display the result in percentage format.

### 4. Confusion Matrix

Generate confusion matrix using `sklearn`. Display it using `ConfusionMatrixDisplay`. Explain clearly:

- **True Positive**
- **True Negative**
- **False Positive**
- **False Negative**

### 5. Overfitting / Underfitting Analysis

Calculate:

- Training accuracy
- Testing accuracy

Compare both and comment whether the model is overfitting or underfitting.

### 6. Hyperparameter Tuning — `max_depth`

Train three Decision Tree models with:

- `max_depth = 1`
- `max_depth = 3`
- `max_depth = None`

Compare their testing accuracies and write your observations.

### 7. Predict for a New Student

Use the trained model to predict the result for a student with:

- `StudyHours = 6`
- `Attendance = 85`
- `PreviousScore = 66`
- `AssignmentsCompleted = 7`
- `SleepHours = 7`

Will the student **Pass** or **Fail**?

### 8. Complete Structured Program

Write a single structured Python program that performs:

1. Dataset loading
2. Data analysis
3. Visualization
4. Train-test split
5. Model training
6. Prediction
7. Accuracy calculation
8. Confusion matrix generation
9. Final conclusion

---

## Program Output

### Output from `assignment39_prg1.py`

```
python assignment39_prg1.py
----------------------------------------
Step 1: Load Data set: 
----------------------------------------
   StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
0         2.0          65             45                     3           5            0
1         3.0          70             50                     4           6            0
2         4.0          75             55                     5           6            0
3         5.0          80             60                     6           7            1
4         6.0          85             65                     7           7            1
    StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
0          2.0          65             45                     3           5            0
1          3.0          70             50                     4           6            0
2          4.0          75             55                     5           6            0
3          5.0          80             60                     6           7            1
4          6.0          85             65                     7           7            1
5          7.0          90             70                     8           8            1
6          8.0          92             75                     9           8            1
7          1.0          60             40                     2           5            0
8          2.5          68             48                     3           6            0
9          3.5          72             52                     4           6            0
10         4.5          78             58                     5           7            1
11         5.5          82             63                     6           7            1
12         6.5          88             68                     7           8            1
13         7.5          93             74                     8           8            1
14         8.5          95             80                     9           8            1
15         1.5          62             42                     2           5            0
16         2.2          67             47                     3           6            0
17         3.8          74             53                     4           6            0
18         4.8          79             59                     5           7            1
19         5.8          83             64                     6           7            1
20         6.8          89             69                     7           8            1
21         7.8          94             76                     8           8            1
22         2.1          66             46                     3           5            0
23         3.2          71             51                     4           6            0
24         4.2          76             56                     5           6            1
25         5.2          81             61                     6           7            1
26         6.2          87             66                     7           7            1
27         7.2          91             72                     8           8            1
28         8.2          96             78                     9           8            1
29         1.8          63             44                     2           5            0
----------------------------------------
Step 2: Data Analysis (EDS)
----------------------------------------
Shape of dataset:  (30, 6)
Colunm Name:  ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours', 'FinalResult']
Missing values (per column)
StudyHours              0
Attendance              0
PreviousScore           0
AssignmentsCompleted    0
SleepHours              0
FinalResult             0
dtype: int64
Statistical report of dataset
       StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
count   30.000000   30.000000      30.000000             30.000000   30.000000    30.000000
mean     4.843333   79.066667      59.566667              5.500000    6.700000     0.600000
std      2.239101   10.973112      11.634323              2.224472    1.087547     0.498273
min      1.000000   60.000000      40.000000              2.000000    5.000000     0.000000
25%      3.050000   70.250000      50.250000              4.000000    6.000000     0.000000
50%      4.900000   79.500000      59.500000              5.500000    7.000000     1.000000
75%      6.725000   88.750000      68.750000              7.000000    8.000000     1.000000
max      8.500000   96.000000      80.000000              9.000000    8.000000     1.000000
----------------------------------------
 Step 3: Decide independant and Dependant veriables
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
Missing values (per column)
StudyHours              0
Attendance              0
PreviousScore           0
AssignmentsCompleted    0
SleepHours              0
FinalResult             0
dtype: int64
----------------------------------------
Step5: Split the Data set for training and testing
----------------------------------------
Shape of x_train:  (24, 5)
Shape of x_test:  (6, 5)
Shape of y_test:  (6,)
Shape of y_train:  (24,)
Model Sucessfully created:  DecisionTreeClassifier(max_depth=5, random_state=42)
----------------------------------------
Step 6: Train the model
----------------------------------------
Model traning complted
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
Confusion Matrics: 
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
Step 9: Plot confusion Matrix
----------------------------------------
```

> Your code should include proper comments explaining each step.