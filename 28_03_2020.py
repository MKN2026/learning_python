# The date today is 28th of March 2020.

# Number Set
global num_set
num_set = [28,54,79,37,2,9,0]
print(num_set)

# Mathematical Function

# Number of items
print("This list contains", len(num_set), "items")

# Largest Number
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

# Adding new items to the list
new_set = int(42, 39, 2, 421, 63)
num_set.append(new_set)
print("this is the new list", num_set)

# Running the code again














print("----------------------------------------------------------------------------")

# Creating a random number between 1 and 100
import random
print(random.randrange(1,100))

# booleans and if commands
x = 59
y = 78

if x > y:
    print ("x is greater than y")
else: 
    print ("y is greater than x")

a = 78
b = 96

if a == b:
    print("a and b are same")
else:
    print("a and b are different")

q = 74
r = 74

if q != r:
    print("q and r are different")
else:
    print ("q and r are same")



