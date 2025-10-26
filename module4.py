N = int(input("Enter a positive integer N: "))

# Create an empty list
numbers = []

# Ask the user to provide N numbers
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask the user 
X = int(input("Enter an integer X: "))

# Check if X is among the numbers
if X in numbers:
    print(f"The index of {X} is: {numbers.index(X) + 1}")  
else:
    print("-1")
