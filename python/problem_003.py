## Problem 3

def is_divisible_by(n, m):
    return 0 == n % m

def largest_prime_factor(n):
    largest = 2
    if n == 1:
        return 1
    else:
        while not n == 1:
            if is_divisible_by(n, largest):
                n = n / largest
            else:
                largest = largest + 1
        return largest


sol = largest_prime_factor(600851475143)

print("SOLUTION: " + str(sol) + "\n")

## SOLUTION: 6857
