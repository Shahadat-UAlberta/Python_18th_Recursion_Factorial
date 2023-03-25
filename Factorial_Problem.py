 # """
# 5! = 1 * 2 * 3 * 4 * 5
# 0! =
# -> Base Case: n==1 -> 1 || n === 0 -> 1
#
# -> recursive case : n * fact(n-1)
# """
#
#
# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# print(fact(1))
#
# """
# Assignment:
#
# N - User Input
#
# 1 - N
#
# Odd Number using Recursion
# """
#
#


def is_odd(num):
    if num == 0:
        return False
    elif num == 1:
        return True
    else:
        return is_odd(num - 2)

user_input = int(input("Enter a number: "))
if is_odd(user_input):
    print(f"{user_input} is odd.")
else:
    print(f"{user_input} is even.")