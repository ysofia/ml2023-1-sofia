import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def main():
    # Read N
    N = int(input("Enter the value of N (positive integer): "))
    while N <= 0:
        print("Error: N should be greater than 0.")
        N = int(input("Enter the value of N (positive integer): "))     
    
    # Read k
    k = int(input("Enter the value of k (positive integer): "))
    while k > N:
        print("Error: k should be less than or equal to N.")
        k = int(input("Enter the value of k (positive integer): "))

    # Read N (x, y) points
    points = []
    for _ in range(N):
        x = float(input(f"Enter x value for point {_ + 1}: "))
        y = float(input(f"Enter y value for point {_ + 1}: "))
        points.append([x, y])

    # Separate the x and y values
    X = np.array([point[0] for point in points]).reshape(-1, 1)
    y = np.array([point[1] for point in points])

    # Ask for the prediction point
    X_pred = float(input("Enter X for prediction: "))
    
    # Use k-NN Regression to predict y
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X, y)
    y_pred = knn_regressor.predict(np.array([[X_pred]]))

    # Compute the coefficient of determination
    y_actual_pred = knn_regressor.predict(X)
    r2 = r2_score(y, y_actual_pred)

    print("Predicted Y value:", y_pred[0])
    print("Coefficient of determination (R^2):", r2)

if __name__ == "__main__":
    main()
