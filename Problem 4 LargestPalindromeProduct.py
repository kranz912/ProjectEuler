def CheckIfNumberIsPalindrome(x):
    Reverse=0
    Number=x
    while(Number>0):
        Reminder = Number%10
        Reverse = (Reverse *10) + Reminder
        Number= Number//10
    return x==Reverse
def getLargestPalindrome(min,max):
    largest=0
    for x in range(min,max):
        for y in range(min,max):
            product= y*x
            isPalindrome = CheckIfNumberIsPalindrome(product)
            if(isPalindrome):
                if(product>largest):
                    largest= product
    return largest
print(getLargestPalindrome(100,1000))