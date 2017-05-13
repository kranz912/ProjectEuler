flag=False
for m in range(500):
    for n in range(m):
        if (m * (m + n) == 500):
            flag= True
            break
    if(flag):
        break
a= m*m -n*n
b= 2*m*n
c= m*m + n*n
print(a*b*c)