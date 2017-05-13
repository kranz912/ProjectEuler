# ProjectEuler
Solving Euler problems

Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems. (https://projecteuler.net/about)

I will be using python for this challenge

### Problem 1: 	Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

```python
sum =0;
for x in range(3,1000):
    if(x%3==0 or x%5 == 0):
        sum+=x
print(sum)
```
### Problem 2: 	Even Fibonacci numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

```python
numbers=[1,1];
x=0;
sum=0
while(True):
    if(x!=0):
        n= numbers[x] + numbers[x-1]
        if (n > 4 * 10 ** 6):
            break
        numbers.append(n)
        if(n%2==0):
            sum+=n;
    x += 1
print(sum)
```
the solution above can be solved using a recursive function for computing the fibbonaci value of n, but since it will be ineffienct having O(n^2) runtime. I used an array to store the previous numbers to have O(n) runtime but having additional space of O(n).

### Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

```python
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
```

Since we continue to divide the input the solution has a runtime of O(log n).
example:
```python
x=8
x/2 = 4 largest= 2
x/2 = 2 largest =2
x/2 = 1 largest =2
```
we only incremented 3 times in this case and log 8 base 2 is = 3

### Problem 4: 	Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
#### Solution 1
```python
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
```
The above solution is slower since it checks the digits twice. ex y=200 x=300 y*x =600, and y=300 x=200 y\*x= 600
reversing the digits when checking if it is a palindrome will have a runtime complexity of O(k) where k is the number of digits.
Instead we can convert it to a string and compare the first element to the last element that way we can have a runtime complexity of O(k/2) which is applied to solution 2.
#### Solution 2
```python
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
```
### Problem 5: Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
```python
i=20
while(True):
    if(i%20==0 and i%19==0 and i%18==0 and i%17==0 and i%16==0 and i%15==0 and i%14==0 and i%13==0 and i%12==0 and i%11==0):
        break
    i+=20
print(i)
```

### Problem 6: Sum Square Difference
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#### Solution 1:
```python
sumofSqr=0
sum=0
SqrofSum=0
for x in range(1,101):
    sumofSqr+=x*x
    sum+=x
    print(x)
SqrofSum= sum*sum;
diff = SqrofSum-sumofSqr
print(diff)
```

#### Solution 2:
```python
limit =100
sum1= limit*(limit+1)/2
sum_sq= (2*limit+1)*(limit+1)*limit/6
print(sum1*sum1-sum_sq)
```

### Problem 7: 10001st Prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

```python
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
```
### Problem 8: Largest product in a series
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

```python

a = """
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    """
start=0
end=13
largest=0
a= a.replace('\n','').replace('\r','').replace(' ','')
while(True):
    digits = ''
    product=1
    if(end>len(a)):
        break
    for x in range(start,end):
            product*=int(a[x])
            digits+=a[x]
    if(product>largest):
        largest= product
    print(digits)
    start+=1
    end+=1
print(largest)
```

### Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

```python
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
```