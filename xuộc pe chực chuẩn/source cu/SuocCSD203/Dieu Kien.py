#1 no case senstitive
if name[-1].lower()=='z':
    return

#2 is a fibonacci number
def is_fibonacci_number(self,num):
    if num<0:
        return False:
    a,b=0,1
    while b<num:
        a,b=b,a+b
    return b==num
    pass

#3 iss a perfect number (số hoàn hảo)
def isPerfectNumber(self,num):
    if num<=0:
        return False
    divisors_sum=0
    for i in range(1,num):
        if num%i==0:
            divisors_sum+=i
    return divisors_sum==num
    pass
#4 is a prime number ( số nguyên tố )
def is_prime(self, number):
    if number<2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i==0:
            return False
    return True

def is_composite(self, number):
    if number<4:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i==0:
            return True
    return False

def is_square(self, number):
    if number<0:
        return False
    sqrt=int(number**0.5)
    return sqrt*sqrt==number

def is_armstrong(self,number):
    num_str=str(number)
    power_sum=sum([int(digit)**len(num_str) for digit in num_str])
    return number == power_sum

# Palindrome Program in Python using Built-in Function
 
def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))
 
# Get the number from the user
n = int(input("Enter number: "))
 
# Check if the number is a palindrome
if is_palindrome(n):
  print("The number is a palindrome!")
else:
  print("The number is not a palindrome.")
