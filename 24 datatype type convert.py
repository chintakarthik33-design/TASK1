# 1. int to float
a = 10
b = float(a)
print(b, type(b))  # 10.0 <class 'float'>

# 2. int to str
a = 10
b = str(a)
print(b, type(b))  # '10' <class 'str'>

# 3. int to bool
a = 1
b = bool(a)
print(b, type(b))  # True <class 'bool'>
# 0 -> False, non-zero -> True

# 4. float to int
a = 10.8
b = int(a)
print(b, type(b))  # 10 <class 'int'>

# 5. float to str
a = 10.5
b = str(a)
print(b, type(b))  # '10.5' <class 'str'>

# 6. float to bool
a = 0.0
b = bool(a)
print(b, type(b))  # False <class 'bool'>

# 7. str to int
a = "25"
b = int(a)
print(b, type(b))  # 25 <class 'int'>

# 8. str to float
a = "25.5"
b = float(a)
print(b, type(b))  # 25.5 <class 'float'>

# 9. str to bool
a = "hello"
b = bool(a)
print(b, type(b))  # True <class 'bool'>
# Empty string "" -> False

# 10. bool to int
a = True
b = int(a)
print(b, type(b))  # 1 <class 'int'>  # False -> 0

# 11. bool to float
a = True
b = float(a)
print(b, type(b))  # 1.0 <class 'float'>

# 12. bool to str
a = False
b = str(a)
print(b, type(b))  # 'False' <class 'str'>

# 13. int to complex
a = 5
b = complex(a)
print(b, type(b))  # (5+0j) <class 'complex'>

# 14. float to complex
a = 5.5
b = complex(a)
print(b, type(b))  # (5.5+0j) <class 'complex'>

# 15. str to list
a = "hello"
b = list(a)
print(b, type(b))  # ['h','e','l','l','o'] <class 'list'>

# 16. str to tuple
a = "hello"
b = tuple(a)
print(b, type(b))  # ('h','e','l','l','o') <class 'tuple'>

# 17. str to set
a = "hello"
b = set(a)
print(b, type(b))  # {'h','e','l','o'} <class 'set'>

# 18. list to str
a = ['a', 'b', 'c']
b = str(a)
print(b, type(b))  # "['a', 'b', 'c']" <class 'str'>

# 19. list to tuple
a = [1, 2, 3]
b = tuple(a)
print(b, type(b))  # (1, 2, 3) <class 'tuple'>

# 20. list to set
a = [1, 2, 2, 3]
b = set(a)
print(b, type(b))  # {1, 2, 3} <class 'set'>

# 21. tuple to list
a = (1, 2, 3)
b = list(a)
print(b, type(b))  # [1, 2, 3] <class 'list'>

# 22. tuple to set
a = (1, 2, 2, 3)
b = set(a)
print(b, type(b))  # {1, 2, 3} <class 'set'>

# 23. set to list
a = {1, 2, 3}
b = list(a)
print(b, type(b))  # [1, 2, 3] <class 'list'>

# 24. set to tuple
a = {1, 2, 3}
b = tuple(a)
print(b, type(b))  # (1, 2, 3) <class 'tuple'>