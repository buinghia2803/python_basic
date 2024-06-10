"""
    + tuple: là 1 bộ giá trị, cấu trúc dữ liệu mà có thứ tự, có thể chứa các phần tử trùng lặp, được tạo bởi dấu ngoặc tròn.
        (tương tự với list nhưng không thể thay đổi bản thân nó và các giá trị bên trong nó)
    + set: không có thứ tự (key), không chứa các phần tử trùng lặp, được tạo bởi dấu ngoặc nhọn.
"""

# tuple

tup1 = 1, 2, 3
print(type(tup1)) # tuple

tup2 = (1, 2, 3)
print(type(tup2)) # tuple

tup3 = 1, 
print(type(tup3)) # tuple

tup4 = (4,) 
print(type(tup4)) # tuple

tup1 = 1, 2, 3
print(tup1[0]) # 1
print(tup1[-1]) # 3

tup1 += (4, 5, 6, 1)
print(tup1) # (1, 2, 3, 4, 5, 6, 1)

#--------------------------

# set

set1 = set()
print(len(set1)) # 0

set1.add(1)
set1.add(1)
set1.add(1)
set1.add(1)

set1.update([2, 3, 4, 5]) # {1, 2, 3, 4, 5}
print(set1) # {1}

set1.remove(1)
print(set1) # {2, 3, 4, 5}

set2 = set1.copy()
print(set1 is set2) # False
print(set1 == set2) # True

set1.clear()
print(set1) # set()

set1 = {1, 2, 3, 4}
set1.add("Kenny")
print(type(set1))
print(set1)

set1 = {1, 2, 3, -10}
any_value = set1.pop() # xóa 1 phần từ bất kỳ, đến hết thì lỗi
print(any_value)
print(set1)

t = 4, 5
a, b = t
print(a) # 4

friends = [
    ('Bob', 23),
    ('Anna', 35),
    ('Henry', 34)
]

print(friends[0][1])

from copy import deepcopy

lst = [[1, [2, 3]], (2, 4)]
# lst1 = lst[:] # dùng cái này ko copy được sâu bên trong chỉ đc [] ở ngoài cùng
lst1 = deepcopy(lst)

print(lst is lst1) # False

lst[0][1].append(100)

print(lst1)

# ----------------------

# 1 cách nữa kiểm tra type
print(isinstance(3, int))

print(ord('a') ^ ord('3')) # XOR 1 ^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1

print(abs(-1)) # 1 # gia tri tuyet doi
print(abs(True)) # 1

print(abs(1+2j)) # canbac2(1^2 + 2^2) = can(5)

print(repr('a')) # 'a'

s = 'a'
a = 3
print(f"{s!r}") # 'a' # phân biệt kiểu chuỗi và số
print(f"{a!r}") # 3

# kít hoạt môi trường ảo: python -m venv venv, ctrl + j