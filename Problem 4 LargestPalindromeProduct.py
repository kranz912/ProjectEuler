import threading
lock = threading.Lock()
def CheckIfNumberIsPalindrome(x):
    Reverse=0
    Number=x
    while(Number>0):
        Reminder = Number%10
        Reverse = (Reverse *10) + Reminder
        Number= Number//10
    return x==Reverse
def getLargestPalindrome():
    largest=0
    for x in range(100,1000):
        for y in range(100,1000):
            product= y*x
            isPalindrome = CheckIfNumberIsPalindrome(product)
            if(isPalindrome):
                if(product>largest):
                    largest= product
                    print(largest)
    return largest

getLargestPalindrome()