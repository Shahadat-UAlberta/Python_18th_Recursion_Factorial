# Write a Python function to sum all the numbers in a list.
#
# Must have:
# 1. Loop
# 2. Function
#
# Note:
# 1. Good to have List User Input
def sum_list(num1):
    sum = 0
    for num in num1:
        sum += num
    return sum
user_input = input("Enter a list of numbers separated by commas: ")
num_list = [int(num) for num in user_input.split(",")]
print("The sum of the numbers is:", sum_list(num_list))
