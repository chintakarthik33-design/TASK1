# Input: digits = [1][2][3]
# leetcode 66 plus one
digits = [1, 2, 3]
a = 0
for i in digits:
    a = a * 10 + i
a = a + 1
s = str(a)
result = []
for i in s:
    result.append(int(i))
print(result)