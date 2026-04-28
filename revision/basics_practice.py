# 🔹 1. Sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 🔹 2. Even or Odd
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# 🔹 3. Positive / Negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 🔹 4. Print 1 to N
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(i)

# 🔹 5. String length
a = "apple"
print("Length:", len(a))
