
# FOR ODD NUMBERS :
def rec (n) :
    if n == 1 :
        return n
    elif n % 2 == 0 :
        return rec (n - 1)
    else:
        print(n)
        return rec (n - 1)


num = int(input())
print(rec (num))
print('-------------------------------------')
# FOR EVEN NUMBERS :
def rec (n) :
    if n == 2 :
        return n
    elif n % 2 != 0 :
        return rec (n - 1)
    else :
        print(n)
        return rec (n - 1)

num = int(input())
print(rec (num))
'''
lst = []
def recursion (n) :
    if n == 1 :
        return n
    elif n % 2 == 0 :
        return recursion (n - 1)
    else :
        print(n)
        lst.append(n)
        print(lst)
        return recursion (n - 1)

num = int(input())
print(recursion(num))

'''