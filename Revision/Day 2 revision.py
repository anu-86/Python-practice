#Question 1: Personal Introduction
#Write a Python program that takes a user's name, age, and city as input and displays a short introduction.

name=input()
age=int(input())
city=input()
print(f'My name is {name}')
print(f'I am {age} years old')
print(f'I live in {city}')

#Question 2: Sum of Two Numbers
#Write a Python program that takes two numbers as input and prints their sum.

a=int(input('Enter a first number:'))
b=int(input('Enter a second number:'))
total = a + b
print(total)

#Question 3: Area of a Rectangle
#Write a Python program that takes the length and breadth of a rectangle as input and calculates its area.

a=int(input('Enter rectangle Length:'))
b=int(input('Enter rectangle breadth:'))
area=a*b
print(area)

#Question 4: Even or Odd Number
#Write a Python program that takes a number as input and checks whether it is even or odd.

a=int(input('Enter a number:'))
if a%2==0:
	print('even')
else:
	print('odd')

#Question 5: Positive, Negative, or Zero
#Write a Python program that takes a number as input and determines whether it is:
#Positive Negative Zero

a=int(input('Enter a number :'))
if a>0:
	print('positive number')
elif a==0:
	print('Zero')
else:
	print('Negative number')

#Question 6: Largest of Two Numbers
#Write a Python program that takes two numbers as input and prints the larger number.

a=int(input('Enter first number'))
b=int(input('Enter second number'))
if a>b:
	print(f'{a} is Larger')
elif b>a:
	print(f'{b} is Larger')
else:
	print('Both are equal')

#Question 7: Voting Eligibility Checker
#Write a Python program that takes a person's age as input and checks whether they are eligible to vote.

age=int(input())
if age>=18:
	print('Eligible to vote')
else:
	print('Not eligible to vote')
#Question 8: Student Grade Calculator
#Write a Python program that takes a student's mark as input and assigns a grade based on the following criteria:
#Plain text
'''
90 - 100  → Grade A
75 - 89   → Grade B
50 - 74   → Grade C
35 - 49   → Grade D
Below 35  → Fail
'''
a = int(input('Enter Mark: '))

if a > 100 or a < 0:
    print('Invalid Mark')
elif a >= 90:
    print('Grade A')
elif a >= 75:
    print('Grade B')
elif a >= 50:
    print('Grade C')
elif a >= 35:
    print('Grade D')
else:
    print('Fail')

#Question 9: Simple Calculator
#Write a Python program that takes:
'''First number
Second number
Operator (+, -, *, /)
and performs the selected operation.'''

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
op=input('Enter operator(+,-,*,/)')
if op =='+':
	print(a+b)
elif op=='-':
	print(a-b)
elif op=='*':
	print(a*b)
elif op=='/':
	print(a/b)
else:
	print('invalid operator')

#Question 10: Celsius to Fahrenheit Converter
'''Write a Python program that converts a temperature from Celsius to Fahrenheit.
Formula:
Plain text
Fahrenheit = (Celsius × 9/5) + 32'''

Celsius=float(input('Enter Temperature in celsius'))
Fahrenheit = (Celsius * 9/5) + 32
print(Fahrenheit)
