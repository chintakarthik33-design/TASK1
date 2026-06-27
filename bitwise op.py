# If two values are same, XOR operation output?
# Rule: a ^ a = 0 Same values ni XOR cheste output always 0 vastadi
a = 5
b = 5
result = a ^ b
print(result)  # Output: 0

x = 10
y = 10
print(x ^ y)   # Output: 0

# Perform AND operation with 1 - Even or Odd check?
# Rule: n & 1 = 1 → Odd, n & 1 = 0 → Evenpython
n = 7
if n & 1 == 1:
    print("Odd")   # Output: Odd
else:
    print("Even")

n = 8
print(n & 1)   # Output: 0 → Even

# Practice All Bitwise Operatorspython
a = 10  # Binary: 1010
b = 6   # Binary: 0110

# 1. AND &
print("AND:", a & b)    # 1010 & 0110 = 0010 → 2

# 2. OR |
print("OR:", a | b)     # 1010 | 0110 = 1110 → 14

# 3. XOR ^
print("XOR:", a ^ b)    # 1010 ^ 0110 = 1100 → 12

# 4. NOT ~
print("NOT a:", ~a)     # ~1010 = -(10+1) = -11
print("NOT b:", ~b)     # ~0110 = -(6+1) = -7

# 5. Left Shift <<
print("Left Shift:", a << 1)  # 1010 << 1 = 10100 → 20
print("Left Shift 2:", a << 2)  # 1010 << 2 = 101000 → 40

# 6. Right Shift >>
print("Right Shift:", a >> 1)  # 1010 >> 1 = 0101 → 5
print("Right Shift 2:", a >> 2)  # 1010 >> 2 = 0010 → 2