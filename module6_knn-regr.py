import numpy as np

class KNNRegression:
    def __init__(self, k, data):
        self.k = k
        self.data = data

    def predict(self, x):
        # Calculate distances from x to all points in the data
        distances = np.sqrt(np.sum((self.data[:, :-1] - x)**2, axis=1))
        
        # Get the indices of the k smallest distances
        k_indices = distances.argsort()[:self.k]
        
        # Calculate the mean of the y-values of the k nearest neighbors
        k_nearest_y = self.data[k_indices, -1]
        return np.mean(k_nearest_y)

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
    
    # Convert points to numpy array
    data = np.array(points)

    # Create KNNRegression object
    knn = KNNRegression(k, data)

    # Read X and predict Y
    X = float(input("Enter the value of X to predict Y: "))
    Y = knn.predict(np.array([X]))
    print(f"The predicted Y value for X = {X} using k-NN Regression is: {Y}")

if __name__ == "__main__":
    main()
