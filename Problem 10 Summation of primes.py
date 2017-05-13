import math
def checkIfPrime(x):
    if(x%2==0 and x!=2):
        return False
    for i in range(3,int(math.sqrt(x))+1,2):
        if(x%i==0):
            return False
    return True

i=2
sum=0
while(i<2*10**6):
    if(checkIfPrime(i)):
        sum+=i
    i+=1
print(sum)
