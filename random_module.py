# random Module
import random

# print("The values are....")
print(random.random())

print(random.randint(1, 100))

print(random.randrange(1, 10, 2))
print(random.randrange(1, 10, 2))
print(random.randrange(1, 10, 2))
print(random.randrange(1, 101, 10))

print(random.choice('Internshala'))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(random.shuffle(numbers))
print("numbers =", numbers)

print(random.choice([]))

# end
