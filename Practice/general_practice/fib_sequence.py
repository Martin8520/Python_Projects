def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence


number_of_terms = int(input("Enter a number: "))
fib_sequence = fibonacci(number_of_terms)
print("Fibonacci sequence up to", number_of_terms, "terms:", fib_sequence)
