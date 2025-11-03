class NumberStore:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("N must be a positive integer.")
        self.capacity = capacity
        self._data = []

    def insert(self, value: int) -> None:
        if len(self._data) >= self.capacity:
            raise OverflowError("Cannot insert more numbers")
        self._data.append(value)

    def search_first(self, x: int) -> int:
        for i, v in enumerate(self._data, start=1):
            if v == x:
                return i
        return -1


def _read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            n = int(raw)
            if n <= 0:
                print("Please enter a positive integer (> 0).")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def _read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main() -> None:
    N = _read_positive_int("Enter N (number of integers to read): ")
    store = NumberStore(N)

    for i in range(1, N + 1):
        num = _read_int(f"Enter integer #{i}: ")
        store.insert(num)

    X = _read_int("Enter X (integer to search for): ")
    print(store.search_first(X))


if __name__ == "__main__":
    main()
