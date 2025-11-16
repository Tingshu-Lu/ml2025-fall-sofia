import sys
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def read_positive_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt).strip())
            if val <= 0:
                raise ValueError
            return val
        except ValueError:
            print("Enter a positive integer.")

def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Enter a valid number.")

def main():
    N = read_positive_int("Enter N (number of training points): ")
    k = read_positive_int("Enter k (neighbors for k-NN): ")

    X_arr = np.empty((N, 1), dtype=float)  
    y_arr = np.empty(N, dtype=float)       

    print("\nEnter the training points one by one:")
    for i in range(N):
        x_i = read_float(f"  x[{i+1}]: ")
        y_i = read_float(f"  y[{i+1}]: ")
        X_arr[i, 0] = x_i     # data insertion into NumPy array
        y_arr[i] = y_i

    label_variance = np.var(y_arr, ddof=1) if N > 1 else 0.0
    print(f"\nLabel variance (sample): {label_variance:.6f}")

    if k > N:
        print(f"Error: k ({k}) must be <= N ({N}).")
        sys.exit(1)

    X_query = read_float("\nEnter the query X to predict y: ")

    # Scikit-learn k-NN regressor
    model = KNeighborsRegressor(n_neighbors=k, weights="uniform", metric="minkowski", p=2)
    model.fit(X_arr, y_arr)

    y_pred = model.predict(np.array([[X_query]], dtype=float))[0]
    print(f"\nPrediction for X = {X_query}: y = {y_pred:.6f}")

if __name__ == "__main__":
    main()
