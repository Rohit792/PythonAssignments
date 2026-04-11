"""
Question 8:
Decision Tree Visualization
Use:
from sklearn. tree import plot_tree
Visualize the trained decision tree.
• Which feature appears at the root node?
• Why do you think that feature was selected first?


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
 

def Visualization():
    dataSet = pd.read_csv("student_performance_ml.csv")
    
    x = dataSet.drop("FinalResult", axis= 1)
    y = dataSet[["FinalResult"]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

    model = DecisionTreeClassifier(criterion="gini", max_depth= 5, random_state= 42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_pred, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    displayInformation("Decision Tree Visualization")
    plt.figure(figsize=(8, 5))
    plot_tree(
        model,
        feature_names = x.columns,
        class_names = ['Fail', 'Pass'],
        filled = True,
        rounded = True,
        fontsize = 10
    )
    plt.title("Student Performance Decesion Tree")
    plt.tight_layout()
    plt.savefig("decision_tree.png", dpi=300, bbox_inches='tight')
    plt.show()

    root_feature_index = model.tree_.feature[0]
    root_feature = x.columns[root_feature_index]
    print(f"Root node feature: {root_feature}")
    print(f"\nWhy '{root_feature}' was selected first:")
    print("This feature provides the highest Gini impurity reduction,")
    print("meaning it best separates Pass/Fail students at the first split.")

def main():
   Visualization()

if __name__ == "__main__":
    main()