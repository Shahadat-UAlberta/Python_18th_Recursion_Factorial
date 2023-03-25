def odd(n):
    if n == 1:
        print(1)
        return
    if n % 2 != 0:
        print(n)


start = int(input("ENTER THE MINIMUM LIMIT OF THE RANGE: "))
end = int(input("ENTER THE MAXIMUM LIMIT OF THE RANGE: "))
for x in range(1):
    print("THE ODD NUMBERS BETWEEN THE RANGE ARE:")
for i in range(start, end + 1):
    (odd(i))
