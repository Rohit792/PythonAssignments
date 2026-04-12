# Python Assignment 41

## Machine Learning - K-Nearest Neighbors (KNN) Algorithm

---

## Overview

This assignment implements the **K-Nearest Neighbors (KNN)** classification algorithm from scratch without using any machine learning libraries. The program demonstrates how the value of K affects prediction results.

---

## Question 1: Basic KNN Implementation

Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm. The algorithm should be implemented manually without using any machine learning library.

### Requirements:

The program should:
- Calculate Euclidean distance
- Sort distances
- Select K nearest neighbors
- Predict the class based on majority voting

### Dataset

| Point | X | Y | Label |
|-------|---|---|-------|
| A     | 1 | 2 | Red   |
| B     | 2 | 3 | Red   |
| C     | 3 | 1 | Blue  |
| D     | 6 | 5 | Blue  |
| E     | 5 | 3 | Blue  |

### Tasks

1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label.

### Input Format

```
Enter X coordinate: 2
Enter Y coordinate: 2
```

### Expected Output

```
Nearest Neighbors:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41
Predicted Class: Red
```

---

## Question 2: Impact of K Value

The value of K plays an important role in the KNN algorithm. Write a Python program that demonstrates how prediction changes when K changes.

### Dataset

Use the same dataset as Question 1.

### Tasks

Predict the class of the same new point using:
- K = 1
- K = 3
- K = 5

### Expected Output

```
Prediction Results
K = 1 → Red
K = 3 → Red
K = 5 → Blue
```

**Explain why the prediction changes when K increases.**

---

## Program Output

### Test Input:
```
Enter X Coordinate: 2
Enter Y Coordinate: 2
```

### Output:

```
________________________________________

When K =  1
('A', 1.0, 'Red')
('B', 1.0, 'Red')
('C', 1.4142135623730951, 'Blue')
('E', 3.1622776601683795, 'Blue')
('D', 5.0, 'Blue')

==================================================
Visualizing the Vote Count
==================================================
Neighbors:           Votes Dictionary:
--------------------------------------------------
A → Red            {'Red': 1}
==================================================
K = 1 → Red

Predicted Class: Red
________________________________________
________________________________________

When K =  3
('A', 1.0, 'Red')
('B', 1.0, 'Red')
('C', 1.4142135623730951, 'Blue')
('E', 3.1622776601683795, 'Blue')
('D', 5.0, 'Blue')

==================================================
Visualizing the Vote Count
==================================================
Neighbors:           Votes Dictionary:
--------------------------------------------------
A → Red            {'Red': 1}
B → Red            {'Red': 2}
C → Blue           {'Red': 2, 'Blue': 1}
==================================================
K = 3 → Red

Predicted Class: Red
________________________________________
________________________________________

When K =  5
('A', 1.0, 'Red')
('B', 1.0, 'Red')
('C', 1.4142135623730951, 'Blue')
('E', 3.1622776601683795, 'Blue')
('D', 5.0, 'Blue')

==================================================
Visualizing the Vote Count
==================================================
Neighbors:           Votes Dictionary:
--------------------------------------------------
A → Red            {'Red': 1}
B → Red            {'Red': 2}
C → Blue           {'Red': 2, 'Blue': 1}
E → Blue           {'Red': 2, 'Blue': 2}
D → Blue           {'Red': 2, 'Blue': 3}
==================================================
K = 5 → Blue

Predicted Class: Blue
________________________________________
```

---

## Key Concepts Demonstrated

### 1. Euclidean Distance
Formula: `√((x₂-x₁)² + (y₂-y₁)²)`

Used to calculate the distance between the new point and all existing data points.

### 2. Sorting Algorithm
Distances are sorted in ascending order to identify the nearest neighbors.

### 3. Majority Voting
The class label is determined by counting votes from the K nearest neighbors and selecting the class with the most votes.

### 4. Impact of K Value

**Why predictions change with different K values:**

- **K = 1 (Red)**: Only considers the single closest neighbor (A or B), both are Red.

- **K = 3 (Red)**: Considers 3 nearest neighbors (A, B, C). Two are Red, one is Blue → Red wins.

- **K = 5 (Blue)**: Considers all 5 neighbors (A, B, C, E, D). Two are Red, three are Blue → Blue wins.

**Key Insight:**
- **Small K values** are more sensitive to noise and local patterns
- **Large K values** consider broader regions and may smooth out local variations
- Choosing the right K is crucial for optimal performance

---

## Algorithm Steps

1. **Calculate Distances**: Compute Euclidean distance from new point to all data points
2. **Sort**: Arrange distances in ascending order
3. **Select K Neighbors**: Pick the K closest points
4. **Vote**: Count the class labels among the K neighbors
5. **Predict**: Return the class with the majority votes

---

## Implementation Notes

- No machine learning libraries used (manual implementation)
- Dictionary used for vote counting with `.get()` method
- `max()` function with `key` parameter for finding winner
- Handles edge case where K > dataset size
- Visualizes vote counting process for educational purposes

---

## Learning Outcomes

After completing this assignment, you understand:
- How KNN algorithm works from first principles
- Euclidean distance calculation
- Majority voting mechanism
- Impact of hyperparameter K on predictions
- Trade-offs between small and large K values
- Manual implementation vs library usage
