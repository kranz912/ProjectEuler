sumofSqr=0
sum=0
SqrofSum=0
for x in range(1,101):
    sumofSqr+=x*x
    sum+=x
    print(x)
SqrofSum= sum*sum;
diff = SqrofSum-sumofSqr
print(sum)
print(diff)

limit =100
sum1= limit*(limit+1)/2
sum_sq= (2*limit+1)*(limit+1)*limit/6
print(sum1*sum1-sum_sq)