1.#Create a list [10,20,30,40,50]
#? Print only even index values using loop.

a=[10,20,30,40,50]
for i in range (len(a)):
	 if i % 2 !=0:
	 	 print(i)

2.#Create [1,2,3,4,5]
#? Create a new list with square of only even numbers using list comprehension.

a=[1,2,3,4,5]
b=[i for i in a if i %2==0]

print(b)

3.#Create ["apple","banana","mango","kiwi"]
#? Print only words with length > 5

a=['apple','banana','Mango','kiwi']
for i in range(len(a)):
	 if len(a[i]) > 5:
	 	print(a[i])

4.#Create [5,10,15,20,25]
#? Find the sum of all elements using loop (no built-in sum())

a=[5,10,15,20,25]
total=0
for i in a:
	total=total+i
print(total)

5.'''
Create [2,4,6,8]? Create new list:
if number < 5 → multiply by 2
else → multiply by 3
(using list comprehension)
'''
a=[2,4,6,8]
b=[ i*2 if i<5 else i*3 for i in a ]
print(b)

6.#Create [1,2,3,4,5]? Reverse the list using slicing

a=[1,2,3,4,5]
a.reverse()
print(a)

7.#Create [10,20,30,40]? Print index and value like:
	
a=[10,20,30,40]
for i in range(len(a)):
	print(i,a[i])

8.#Create [1,2,2,3,4,4,5]? Remove duplicates and print new list

a=[1,2,2,3,4,4,5]
a.remove(4)
a.remove(2)
print(a)

9.#Create [5,15,25,35,45]? Count how many values are greater than 20

a=[5,15,25,35,45]
count=0
for i in a:
	if i >20:
	    count=count+1
print(count)

10.#Create [1,2,3,4,5,6]? Create new list with:even numbers → keep same odd numbers → make it 0

a=[1,2,3,4,5,6]
b=[]
for i in a:
	if i%2!=0:
		b.append(0)
	
	else:
		b.append(i)
print(b)


