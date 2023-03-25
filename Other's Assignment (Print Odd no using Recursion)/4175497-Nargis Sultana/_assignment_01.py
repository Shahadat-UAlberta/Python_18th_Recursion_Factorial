#start = 0
#end = int(input("Ente the end limit: "))
def getOdd (n):
        if n == 1 or n == 0:
            return n
        else:
            return n % 2 == 1
num= int(input())
print(getOdd(num))
