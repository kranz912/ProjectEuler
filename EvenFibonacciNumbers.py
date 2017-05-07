numbers=[0,1];
x=0;
while(True):
    if(x!=0):
        n= numbers[x] + numbers[x-1]
        if (n > 4 * 10 ** 6):
            break
        numbers.append(n)
        if(n%2==0):
            print(n)
    x += 1