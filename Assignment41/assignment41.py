"""
Question:

"""
import math

def caculate_euclidean_distance(x, y):
    # Formula: sqrt((x2-x1)^2 + (y2-y1)^2)
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1]) ** 2)

def prediictClass(neighbors):
    classVotes = {}

    print("\n" + "="*50)
    print("Visualizing the Vote Count")
    print("="*50)
    print(f"{'Neighbors:':<20} {'Votes Dictionary:'}")
    print("-"*50)

    for pointName, distance, label in neighbors:
        classVotes[label] = classVotes.get(label, 0) + 1
        print(f"{pointName} → {label:<14} {classVotes}")

    print("="*50)
    return max(classVotes, key = classVotes.get)

def getNearestNeighbours(df, newPoint, k_vlaue):
    distances = []

    for pointName, x, y, lebal in df:
        distance = caculate_euclidean_distance((x, y), newPoint)
        distances.append((pointName, distance, lebal))

    distances.sort(key = lambda x : x[1])
    
    for data in distances:
        print(data)

    return distances[:k_vlaue]

def main():
    dataset = [
        ('A', 1, 2, 'Red'),
        ('B', 2, 3, 'Red'),
        ('C', 3, 1, 'Blue'),
        ('D', 6, 5, 'Blue'),
        ('E', 5, 3, 'Blue')
    ]

    x = float(input("Enter X Coordinate: "))
    y = float(input("Enter Y Coordinate: "))

    newPoints = (x, y)
    k_value = [1, 3, 5]



    for k in k_value:
        print("_"*40)
        print("\nWhen K = ", k)
        effective_k = min(k, len(dataset))
        neighbors = getNearestNeighbours(dataset, newPoints, effective_k)
        predicted_class = prediictClass(neighbors)
        print(f"K = {k} → {predicted_class}")
        print(f"\nPredicted Class: {predicted_class}")
        print("_"*40)
   
    
if __name__ == "__main__":
    main()