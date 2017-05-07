import math
def getprimefactors(x):
    largest=1
    while(x%2==0):
        x=x/2
        largest=2
    for i in range(3,int(math.sqrt(x)),2):
        while(x%i==0):
            largest=i
            x=x/i
    x=int(x)
    if(x>2):
        largest=x
    return largest
print(getprimefactors(13195))