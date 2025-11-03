from module5_mod import NumberStore


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
