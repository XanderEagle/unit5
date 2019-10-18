import random

even_number = 0
odd_number = 0

for x in range(10):
    number = random.randint(1, 100)
    print(number)
    if number % 2 == 0:
        even_number = number + even_number
    else:
        odd_number = number + odd_number

print(even_number, odd_number)
