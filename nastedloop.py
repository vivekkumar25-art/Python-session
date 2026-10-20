# Nested Loops: Prime Numbers

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

# o/t - 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47



## Fibonacci Sequence

a, b = 0, 1
count = 0

while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1


# o/t - 0 1 1 2 3 5 8 13 21 34
