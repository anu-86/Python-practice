#1️⃣ Even or Odd#Take a number from user and print whether it is even or odd.

n=(int(input('Enter a Number:')))
if n%2==0:
	print('Even')
else:
	print('odd')
	
	
#2️⃣ Largest of Two Numbers Input 2 numbers and print the largest.

a=int(input('Enter a number'))
b=int(input('Enter a nunber'))
print(max(a,b))

#3️⃣ Largest of Three Numbersb#Input 3 numbers and find the biggest using if-elif-else.

a=int(input('Enter a number'))
b=int(input('Enter a number'))
c=int(input('Enter a number'))
if a>b and a>c:
	print('a is highest number')
elif b>a and b>c:
	print('b is  highest number')
else:
	print('c is highest number')
