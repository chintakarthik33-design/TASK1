# TASK: 13/06/2026 
#Square Pattern pythonn
n=5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
#Right Trianglepythonn
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
#Number Trianglepythonn
n=5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
# Repeated Number Trianglepythonn
n=5
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
#Alphabet Trianglepythonn
n=5
for i in range(1, n+1):
    val = 65
    for j in range(i):
        print(chr(val), end=" ")
        val += 1
    print()
#Inverted Star Trianglepythonn
n=5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

#Inverted Number Trianglepythonn
n=5
for i in range(n):
    for j in range(1, n-i+1):
        print(j, end=" ")
    print()
#Continuous Number Patternpythonn
n=5
val = 1
for i in range(1, n+1):
    for j in range(i):
        print(val, end=" ")
        val += 1
    print()
#Right-Aligned Star Trianglepythonn
n=5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
#Pyramid Patternpythonn
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()