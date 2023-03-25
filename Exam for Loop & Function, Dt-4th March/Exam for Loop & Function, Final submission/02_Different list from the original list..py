# Create a Python function that takes a list and produces a new list with members that are different from the ones in the original list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
# ---
# Must have:
# 1. Loop
# 2. Function
#
# Note:
# 1. Good to have List User Input

def new_list(num1):
    new_numbers = []
    for num in num1:
        if num not in new_numbers:
           new_numbers.append(num)
    return new_numbers

user_input = input("Enter a list of numbers separated by commas: ")
num_list = [int(num) for num in user_input.split(",")]
new_num_list = new_list(num_list)
print("The unique numbers are:", new_num_list)