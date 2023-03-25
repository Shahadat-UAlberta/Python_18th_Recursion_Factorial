def odd(num):

    if num == 0:
        return 0
    else:
     odd(num - 1)    # recursion
    if num % 2 == 1:
        print(num)


odd(int(input("Enter an Integer: ")))
