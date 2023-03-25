

def getodd(n):

    if n == 0:
        return 
       
    if n % 2 == 1:
        print(n)
        getodd(n-1) 
    else:
        getodd(n-1)
        

getodd(int(input("Enter an Integer: ")))

