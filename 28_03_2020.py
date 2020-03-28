# The date today is 28th of March 2020.

# Number Set
global num_set
num_set = [28,54,79,37,2,9,0]
print(num_set)

# Lagest Number
largest_num = (max(num_set))
print("The largest number is", largest_num)

# Smallest Number
smallest_num = (min(num_set))
print("The smallest number is", smallest_num)

# Sum total of all numbers
print("The total of these numbers is",sum(num_set))

# Division of third and fourth digits
# Seperating the digits
div_num = (num_set[2], num_set[3])
print("we are going to divide", div_num)
ans = (divmod(num_set[2], num_set[3]))
print("the answer for 79 divide by 37 is", ans)

""" Playing with RANDOM """

# Creating a random number between 1 and 100
import random

print(random.randrange(1,100))



