import math
def getprimefactors(x):
    largest=1
    while(x%2==0):
        x=x/2
        largest=2
    for i in range(3,int(math.sqrt(x))+1,2):
        while(x%i==0):
            largest=i
            x=x/i
    x=int(x)
    if(x>2):
        largest=x
    return largest
def checkIfPrime(n):
    if(getprimefactors(n)==n):
        return True
    return False
x=0
y=2
while(True):
    if(checkIfPrime(y)):
        x+=1
        print("{0}:{1}".format(x,y))
    if(x==10001):
        break
    y+=1
print(y)