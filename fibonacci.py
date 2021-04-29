# Program to generate Fibonacci series until the 20th value
def fibonacci(a):
    if a <= 1:
        return a
    else:
        return fibonacci(a-1) + fibonacci(a-2)


# defining end parameter
number_of_terms = 20

# check if the number of terms is valid
if number_of_terms <= 0:
    print("Please enter a positive integer")
else:
    # displaying the output of a fibonacci sequence
    print("Fibonacci sequence:")
    for i in range(number_of_terms):
        print(fibonacci(i), end=" ")
