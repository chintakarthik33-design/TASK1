# 1. Positive or Negative or Zero
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

print("-----")

# 2. Upper or Lower case
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print("Upper case")
elif 'a' <= ch <= 'z':
    print("Lower case")
else:
    print("Not an alphabet")

print("-----")

# 3. Pass or Fail for 6 subjects
s1 = int(input("Subject 1: "))
s2 = int(input("Subject 2: "))
s3 = int(input("Subject 3: "))
s4 = int(input("Subject 4: "))
s5 = int(input("Subject 5: "))
s6 = int(input("Subject 6: "))

if s1 > 35 and s2 > 35 and s3 > 35 and s4 > 35 and s5 > 35 and s6 > 35:
    print("Pass")
else:
    print("Fail")  