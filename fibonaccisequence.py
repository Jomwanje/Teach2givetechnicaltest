# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci_sequence(1000))
