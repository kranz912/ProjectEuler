def CheckIfNumberIsPalindrome(x):
    ispalindrome=True
    i=0
    x=str(x)
    while((i<len(x)/2) and ispalindrome):
        if(x[i]!=x[-(i+1)]):
            ispalindrome= False
        i+=1
    return ispalindrome
def getLargestPalindrome(min,max):
    largest=0
    for x in range(max,min,-1):
        for y in range(x,min,-1):
            product= y*x
            if (product > largest):
                isPalindrome = CheckIfNumberIsPalindrome(product)
                if(isPalindrome):
                    largest= product
            else:
                break
    return largest
print(getLargestPalindrome(100,1000))
