def odd(num):
    if num == 0:
        return
    elif num == 1:
        print(num)
        return 1
    elif num % 2 == 1:
        odd(num - 2)
        print(num)
        return num

    else:
        # odd(num - 1)
        return odd(num - 1)

user_input = int(input())
odd(user_input)