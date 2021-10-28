#author- Shreyas Agrawal
#Date- 7 Aug 2018
#Factorial Task

print('Hey!')

name=input('What is your name?\n')
print('Hello', name,'!')
enter=input('Click enter to continue')

think=input('Think of 3 numbers from 1 to 10, then hit enter')
number=int(input("Enter the 1st number to find it's factorial\n"))

def factorial (n):
    if n==0:
        return 1
    else:
        return n * factorial (n-1)

print('The answer is...')
print(factorial(number))

number2=int(input("Enter the 2nd number to find out it's factorial\n"))

print('The answer is...')
print(factorial(number2))


number3=int(input("Enter the 3rd number to find out it's factorial\n"))

print('The answer is...')
print(factorial(number3))

