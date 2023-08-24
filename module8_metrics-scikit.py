import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Read N
    N = int(input("Enter the value of N (positive integer): "))
    while N <= 0:
        print("Error: N should be greater than 0.")
        N = int(input("Enter the value of N (positive integer): "))     

    # Read N (x, y) points
    points = []
    for _ in range(N):
        x = int(input(f"Enter x value for point {_ + 1}: "))
        while x != 1 and x != 0:
          print("Error: x should be 0 or 1.")
          x = int(input(f"Enter x value for point {_ + 1}: "))
        y = int(input(f"Enter y value for point {_ + 1}: "))
        while y != 1 and y != 0:
          print("Error: y should be 0 or 1.")
          y = int(input(f"Enter y value for point {_ + 1}: "))      
        points.append([x, y])

    # Separate the x and y values
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])

    # Calculate Precision and Recall using Scikit-learn
    precision = precision_score(x, y)
    recall = recall_score(x, y)

    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")

if __name__ == "__main__":
    main()
