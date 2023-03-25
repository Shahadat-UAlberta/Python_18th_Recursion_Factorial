#
# #https://www.naukri.com/learning/articles/for-loop-in-python-examples/#1
#
# #Example 1: Print the first 10 natural numbers using for loop.
#
num = int(input())

for value in range (1, 11): #num + 1):
    print(value)
    #value = (num + 1)

# #Example 2: Python program to print all the even numbers within the given range.
#
# num = int(input())
#
# for value in range (1, num):
#     if value % 2 == 1:
#         print(value)
#     else:
#         pass

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

# num = int(input())
# sum = 0
# for value in range (1, num+1):
#     sum+=value
#     print(sum)

# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
#
# num = int(input())
# sum = 0
# for value in range (1, num+1):
#     if value % 2 == 1:
#         #n=value
#         sum+=value
#     print(sum)


# # if the given range is 10
# given_range = 10
#
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
#
# for i in range(given_range):
#
#     # if i is odd, add it
#     # to the sum variable
#     if i % 2 != 0:
#         sum += i
#
# # print the total sum at the end
#     print(sum)

# Example 5: Python program to print a multiplication table of a given number

# num = int(input())
# mul=1
# for value in range (1, num+1):
#     mul*=value
#     print(mul)

# # Example 6: Python program to display numbers from a list using a for loop.
#
# lst= [2, 3, 5, 7, 9, 12]
#
# # for value in lst:
#
# for value in range (lst[0:]):
#     print(value)

# Example 7: Python program to count the total number of digits in a number.
num = 125
num = str(num)
sum = 0
for value in num:
    sum+=1
print(sum)
