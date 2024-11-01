def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Input from the user
terms = int(input("Enter the number of terms in Fibonacci series: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The Fibonacci series up to {terms} terms is: {fibonacci_iterative(terms)}")
