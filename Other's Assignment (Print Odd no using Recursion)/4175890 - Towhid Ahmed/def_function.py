




num=int(input("Enter: "))

def recur(n,c=1):

    if n==0:
        return 0
    elif c<=n:
        print(2*c-1)
        recur(n,c+1)
    return

recur(num)

