# sum of digits
n = 1234
sum = 0
while n > 0:
    sum += n % 10   # last digit teesukuntam
    n //= 10        # last digit remove chestam
print(sum)  # 10

#revers a number 
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)  # 4321

#check even or odd
n = 17
if n % 2 == 0:
    print("Even")
else:
    print("Odd")  # Odd

#count digits in a number 
n = 12345
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)  # 5
# Shortcut: print(len(str(12345)))

#check prime number

n = 13
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
print("Prime" if is_prime else "Not Prime")  # Prime

#find factorial 
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)  # 120

#find factors
n = 12
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=", ")  # 1, 2, 3, 4, 6, 12,

#check palindrome
n = 121
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
if temp == rev:
    print("Palindrome")  # Palindrome
else:
    print("Not Palindrome")

#check armstrong number
n = 153
temp = n
sum = 0
digits = len(str(n))
while n > 0:
    sum += (n % 10) ** digits
    n //= 10
if temp == sum:
    print("Armstrong")  # Armstrong
else:
    print("Not Armstrong")

#GCD AND HCF
a, b = 12, 18
while b:
    a, b = b, a % b 
print(a)  # 6

#convert binary to decimal
binary = input("Enter binary number: ")  # Ex: 1011
decimal = 0