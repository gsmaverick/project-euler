# Problem 3:
#   The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143?

import utils

number = 600851475143
counter = 600851475143
primes = []

for x in utils.gen_primes():
    # Break out of the loop if the square of the number
    # if larger than the original value being checked against.
    if (x * x) > counter:
        break
    elif number % x == 0:
        primes.append(x)
        number = number / x

# Return the largest prime factor that was found.
print primes[-1]