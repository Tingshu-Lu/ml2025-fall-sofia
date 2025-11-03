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

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"NumberStore(capacity={self.capacity}, data={self._data})"
