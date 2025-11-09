import numpy as np

class KNNRegressor1D:
    def __init__(self):
        self.x = None  
        self.y = None  

    def fit(self, x, y):
        x = np.asarray(x, dtype=float).reshape(-1)
        y = np.asarray(y, dtype=float).reshape(-1)
        if x.shape != y.shape:
            raise ValueError("x and y must have the same length.")
        if x.size == 0:
            raise ValueError("Training data cannot be empty.")
        self.x, self.y = x, y

    def predict(self, x_query, k):
        if self.x is None or self.y is None:
            raise ValueError("Model has not been fit yet.")
        if not (isinstance(k, int) and k > 0):
            raise ValueError("k must be a positive integer.")
        n = self.x.size
        if k > n:
            raise ValueError(f"k (={k}) must be <= N (={n}).")

        dists = np.abs(self.x - float(x_query))  
        nn_idx = np.argpartition(dists, k - 1)[:k]

        nn_idx = nn_idx[np.argsort(dists[nn_idx], kind="stable")]
        return float(np.mean(self.y[nn_idx]))


def read_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v <= 0:
                print("Please enter a positive integer.")
                continue
            return v
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid input. Please enter a real number")


def main():
    print("k-NN Regression")
    N = read_positive_int("Enter N (number of points, positive integer): ")
    k = read_positive_int("Enter k (positive integer): ")

    x_arr = np.zeros(N, dtype=float)
    y_arr = np.zeros(N, dtype=float)

    print(f"Now enter {N} points as x and y (real numbers):")
    for i in range(N):
        xi = read_float(f"Point {i+1} - x: ")
        yi = read_float(f"Point {i+1} - y: ")
        x_arr[i] = xi
        y_arr[i] = yi

    X_query = read_float("Enter query X (real number): ")

    try:
        knn = KNNRegressor1D()
        knn.fit(x_arr, y_arr)
        y_hat = knn.predict(X_query, k)
        print(f"k-NN Regression prediction at X={X_query}: Y ≈ {y_hat:.6f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
