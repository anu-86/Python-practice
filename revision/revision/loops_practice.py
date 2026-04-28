# 🔹 1. Tuple reverse
n = (1, 2, 3)
print("Reversed tuple:", n[::-1])


# 🔹 2. Palindrome check (string)
n = input("Enter value: ")
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# 🔹 3. Fibonacci series (10 numbers)
a = 0
b = 1
print("Fibonacci:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()


# 🔹 4. Prime number check
n = int(input("Enter number: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")


# 🔹 5. Even numbers from 1 to 100
print("Even numbers:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
