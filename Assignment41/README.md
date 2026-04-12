# Python Assignment 41

## Machine Learning - K-Nearest Neighbors (KNN) Algorithm

---

## Overview

This assignment implements the **K-Nearest Neighbors (KNN)** classification algorithm from scratch without using any machine learning libraries. The program demonstrates how the value of K affects prediction results.

---

## Question 1: Basic KNN Implementation

Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm. The algorithm should be implemented manually without using any machine learning library.

### Requirements

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

### Test Input

```
Enter X Coordinate: 2
Enter Y Coordinate: 2
```

### Output

```
Enter X Coordinate: 2
Enter Y Coordinate: 2

================================================================================
Euclidean Distance Calculation Table
================================================================================
Point    X1       Y1       X2       Y2       EU-Distance    
--------------------------------------------------------------------------------
A        1        2        2.0      2.0      1.0000         
B        2        3        2.0      2.0      1.0000         
C        3        1        2.0      2.0      1.4142         
D        6        5        2.0      2.0      5.0000         
E        5        3        2.0      2.0      3.1623         
================================================================================
________________________________________

When K =  1

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

**Formula:** `√((x₂-x₁)² + (y₂-y₁)²)`

Used to calculate the distance between the new point and all existing data points.

**Example Calculation:**
- Point A (1, 2) to New Point (2, 2): `√((2-1)² + (2-2)²) = √(1 + 0) = 1.0`
- Point C (3, 1) to New Point (2, 2): `√((2-3)² + (2-1)²) = √(1 + 1) = 1.414`

### 2. Sorting Algorithm

Distances are sorted in ascending order to identify the nearest neighbors efficiently.

### 3. Majority Voting

The class label is determined by:
1. Counting votes from the K nearest neighbors
2. Each neighbor votes for its class
3. The class with the most votes wins

**Voting Mechanism:**
```python
classVotes = {}
for neighbor in neighbors:
    classVotes[label] = classVotes.get(label, 0) + 1
winner = max(classVotes, key=classVotes.get)
```

### 4. Impact of K Value

**Why predictions change with different K values:**

| K Value | Neighbors Considered | Red Votes | Blue Votes | Winner |
|---------|---------------------|-----------|------------|--------|
| K = 1   | A                   | 1         | 0          | **Red** |
| K = 3   | A, B, C            | 2         | 1          | **Red** |
| K = 5   | A, B, C, E, D      | 2         | 3          | **Blue** |

**Analysis:**

- **K = 1 (Red)**: Only considers the single closest neighbor (A), which is Red.

- **K = 3 (Red)**: Considers 3 nearest neighbors (A, B, C). Two are Red, one is Blue → Red wins.

- **K = 5 (Blue)**: Considers all 5 neighbors (A, B, C, E, D). Two are Red, three are Blue → Blue wins.

**Key Insights:**
- **Small K values (K=1)** are more sensitive to noise and local outliers
- **Medium K values (K=3)** provide balanced predictions with local context
- **Large K values (K=5)** consider broader regions and capture overall data distribution
- Choosing the right K is crucial for optimal performance
- As K increases, the decision boundary becomes smoother

---

## Algorithm Steps

1. **Input**: Accept new point coordinates (x, y) from user
2. **Calculate Distances**: Compute Euclidean distance from new point to all data points
3. **Sort**: Arrange distances in ascending order
4. **Select K Neighbors**: Pick the K closest points
5. **Vote**: Count the class labels among the K neighbors
6. **Predict**: Return the class with the majority votes

---

## Implementation Details

### Distance Table Display

The program displays a comprehensive table showing:
- Original point coordinates (X1, Y1)
- New point coordinates (X2, Y2)
- Calculated Euclidean distance

This helps visualize how distances are computed before classification.

### Vote Visualization

The program shows step-by-step voting:
- Each neighbor's contribution
- Running vote count
- Final decision

This educational feature helps understand the majority voting mechanism.

### Edge Case Handling

- Uses `effective_k = min(k, len(dataset))` to handle K > dataset size
- Prevents index errors when K exceeds available data points

---

## Technical Implementation

### Functions Used

1. **`caculate_euclidean_distance(x, y)`**
   - Calculates distance between two points
   - Returns: float (distance value)

2. **`print_distance_table(df, newPoint)`**
   - Displays formatted table with distance calculations
   - Shows X1, Y1, X2, Y2, and EU-Distance

3. **`getNearestNeighbours(df, newPoint, k_value)`**
   - Finds K nearest neighbors
   - Returns: list of (pointName, distance, label) tuples

4. **`prediictClass(neighbors)`**
   - Implements majority voting
   - Visualizes vote counting process
   - Returns: predicted class label

### Data Structures

- **Tuple**: Storing point data `(name, x, y, label)`
- **List**: Storing distances and neighbors
- **Dictionary**: Counting votes `{'Red': 2, 'Blue': 1}`

---

## Learning Outcomes

After completing this assignment, you understand:

1. **KNN Algorithm Fundamentals** - How distance-based classification works
2. **Euclidean Distance** - Mathematical formula and implementation
3. **Majority Voting** - Democratic decision-making in ML
4. **Hyperparameter Tuning** - Impact of K on model behavior
5. **Algorithm Visualization** - Displaying intermediate steps for learning
6. **Manual Implementation** - Building ML algorithms from scratch
7. **Trade-offs** - Balancing between local sensitivity and global patterns

---

## Why K Matters?

### Small K (K=1)
- ✅ Captures fine-grained patterns
- ❌ Sensitive to noise and outliers
- ❌ May overfit training data

### Medium K (K=3)
- ✅ Balanced approach
- ✅ Reduces noise impact
- ✅ Good generalization

### Large K (K=5+)
- ✅ Smooth decision boundaries
- ✅ Robust to noise
- ❌ May miss local patterns
- ❌ Computationally expensive

---

## Conclusion

This assignment demonstrates that KNN is a simple yet powerful algorithm where:
- No training phase is required (lazy learning)
- Predictions based on similarity (distance)
- K value significantly affects results
- Manual implementation helps understand ML fundamentals

**Best Practice:** Use cross-validation to find optimal K value for your dataset!
