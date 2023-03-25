# """
# Assignment:
#
# N - User Input
#
# 1 - N
#
# Odd Number using Recursion
# """
def is_odd(n):
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        return is_odd(n-2)

n = int(input("Enter a number: "))
if is_odd(n):
    print(f"{n} is odd.")
else:
    print(f"{n} is even.")



print("----------------")

def check(n):
    if n == 1 or n == 0:
        return (n % 2 == 1)
    else:
        return (check(n - 2))
n=int(input("Enter number:"))
print("is odd,",check(n))
