# The date today is 30th of March 2020.

# Mathematical Function
def maths_function(nums):
    # Showing the set of numbers
    print(nums)
    # Number of Items
    print("This list contains", len(nums), "items")
    # Largest Number
    print("The largest number is", max(nums))
    # Smallest Number
    print("The smallest number is", min(nums))
    # Sum of all numbers
    print("The total of these numbers is",sum(nums))
    # Explain Division
    div_num = (nums[2], nums[3])
    print("we are going to divide", div_num)
    # Divide
    print("the answer for", nums[2], "divide by", nums[3], "is", divmod(nums[2], nums[3]))

# Running the code first time

num_set1 = [28,54,79,37,2,9,0]

maths_function(num_set1)

print("----------------------------------------------------------------------------")

# Running the code with a new list

num_set2 = [784,621,910,521,374,149]

maths_function(num_set2)

print("----------------------------------------------------------------------------")

print("All even numbers from 0 to 100")

for x in range(101):
    if x % 2 == 0:
        print(x, x)
