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
