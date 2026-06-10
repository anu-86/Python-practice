#practice 1:Sum of numbers from 1 to 10
total=0
for i in range(1,11):
	total=total+i
print('sum',total)

#practice 2:Sum of numbers from 1 to 50

total=0
for i in range(1,51):
	total=total+i
print('sum',total)

#Practice 3: Take n from user and find sum from 1 to n
n = int(input("Enter a number: "))
total=0
for i in range(1,n+1):
	total=total+i
print(total)

#practice 4:Check whether a number is Even or Odd.
n=int(input('Enter number:'))
if n%2==0:
	print('Even')
else:
	print('odd')

#practice 5:Print all Even numbers from 1 to n.
n=int(input('Enter number'))
for i in range(2,n+1,2):
	print(i)


#practice 6:Find factorial of a number entered by the user.

n=int(input())
fact=1
for i in range(1,n+1):
	fact=fact*i
print('Factorial',fact)

#practice 7:Find factorial of 6 (without input).

n=6
fact=1
for i in range(1,n+1):
	fact=fact*i
print('Factorial',fact)

#practice 8:print factorials from 1 to 5.
'''Expected:
Plain text
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120'''
n=int(input())
fact=1
for i in range(1,n+1):
	fact=fact*i
	print(i,'!','=',fact)

#practice question 9:Count digits in a user-entered number.
n =int(input())
count=0
while n>0:
	count=count+1
	n=n//10
print('count digits',count)

#practice question 10:Count digits and print:
	
n=234567890
count=0
while n>0:
	count=count+1
	n=n//10
print('Number of digits','=',count)

	
	
