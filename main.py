# # Recursion
#
# """
# - Recursion is a programming technique in which a *function* calls itself one or more times to solve a problem.
# - Two Parts: 1. Base Case and 2. Recursive case
#
# - A loop is control structure that iteratively executes a block of code until a certain condition is met.
# - Recursion, is a technique in which a function calls itself to solve a problem.
#
# - Recursion can be less efficient than loop
# -
# """
#
#
# # Sum of natural numbers using recursion [1 - N]
#
# def getSum(n):
#     if n != 0:
#         return n + getSum(n - 1)
#     else:
#         return n


# num = int(input())  # 5
# print(getSum(num))

def check(n):
    if n == 1 or n == 0:
        return (n % 2 == 1)
    else:
        return (check(n - 2))
n=int(input("Enter number:"))
print("The no is Odd,",check(n))

    # else:
    # print("The no is even")
    #     return ()

# if(check(n)==True):
#       print("Number is even!")
# else:
#       print("Number is odd!")

print("---------------")


def odd(num):
    if num <= 0:
        return
    if num % 2 == 1:
        odd(num - 2)
        # print(num)
        return num

    if num % 2 == 0:
        return odd(num - 1)


for i in range(1, 7):
    print(odd(i))
# num = 10
# print(odd(num))
