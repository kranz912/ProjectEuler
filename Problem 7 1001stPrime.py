import math
def checkIfPrime(x):
    if(x%2==0 and x!=2):
        return False
    for i in range(3,int(math.sqrt(x))+1,2):
        if(x%i==0):
            return False
    return True

x=0
y=2
while(True):
    if(checkIfPrime(y)):
        x+=1
    if(x==10001):
        break
    y+=1
print(y)