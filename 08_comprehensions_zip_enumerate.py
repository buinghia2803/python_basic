"""
    Iterable: list, tuple, set, dict: là những thứ có thể duyệt qua vòng for

    List comprehensions
    Set comprehensions
    Dict comprehensions
    Tuple comprehensions
    => comprehensions luôn tạo ra 1 mảng mới

    zip => trả về các tuple tương ứng
    enumerate => trả về các tuple tương ứng có key là index
"""

# Iterable
lst = [4, 100, 5, 6]

for value in lst:
    print(value)

lst = (4, 100, 5, 6)

for value in lst:
    print(value)

lst = {4, 100, 5, 6}  # ko đảm bảo thứ tự khi được chèn vào

for value in lst:
    print(value)

d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(key)  # trả về key của dict

for value in d.values():
    print(value)  # trả về value của dict

for item in d.items():
    print(item)  # trả về các tuple (key, value) của dict
    key, value = item
    print(key)
    print(value)
    print("-" * 20)

# List comprehensions
lst = [1, 2, 3, 4]

# c1
new_list = []

for x in lst:
    val = x * 2
    new_list.append(val)

print(x)
print(new_list)  # [2, 4, 6, 8]

# c2
new_list = [val * 2 for val in lst]
print(new_list)  # [2, 4, 6, 8]

# Set comprehensions
set_a = {"a", "c", "b"}

new_set = {s.upper() for s in set_a}
print(new_set)

# Dict comprehensions
d = {"a": 1, "b": 2, "c": 3}

new_d = {k: v * 2 for k, v in d.items()}
print(new_d)

# Tuple comprehensions
# Correct way
new_tuple = tuple(x**2 for x in range(5))
print(new_tuple)

# Incorrect way, which creates a generator object inside a tuple
new_tuple = (x**2 for x in range(5))  # This is a generator object, not a tuple
print(new_tuple)

# To get a tuple from the generator object above, you would still need to wrap it with tuple()
new_tuple = tuple((x**2 for x in range(5)))
print(new_tuple)

# zip

lst1 = ["a", "b", "c"]
lst2 = (1, 2, 3, 4)
lst3 = ["a1", "b1"]
print(list(zip(lst1, lst2, lst3)))

print(list(zip(lst1)))  # chú ý
# enumerate
#       0    1    2
#       1    2    3

lst = ["a", "b", "c"]
print(list(enumerate(lst, start=1)))

lst1 = ("a", "b", "c")
lst2 = (1, 2, 3)
print(list(zip(lst1, lst2)))
print(dict(zip(lst1, lst2)))

print("-" * 50)  # ví dụ

numbers = [100, 34, 52, 452, -42, 54, 1, -423]

new_lst = [v for v in numbers if v % 2 != 0]
print(new_lst)
print(sum(new_lst))

new_lst = [v * 2 if v % 2 == 0 else v * 3 for v in numbers]
print(new_lst)

new_lst = []

for x in numbers:
    if x % 2 == 0:
        new_lst.append(x * 2)
    else:
        new_lst.append(x * 3)

print(new_lst)

#      0  1  2  3
lst = [1, 2, 3, 4]

# {i} - {value}
for idx, value in enumerate(lst, start=1):
    # idx, value = item
    print(f"{idx} - {value}")

lst = [1, 2, 3, 4]
# c1
for i in range(len(lst)):
    if i % 2 != 0:
        print(i, lst[i])

# c2
for i, v in enumerate(lst):
    if i % 2 != 0:
        print(i, v)

print("-" * 50)  # bài tập

# c1
odd = even = 0

for n in range(1001):
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Số lượng giá trị chẵn trong [0, 1000]\t: {even}")
print(f"Số lượng giá trị lẻ trong [0, 1000]\t: {odd}")

# c2
even = sum([1 for n in range(1001) if n % 2 == 0])
odd = sum([1 for n in range(1001) if n % 2 != 0])

print(f"Số lượng giá trị chẵn trong [0, 1000]\t: {even}")
print(f"Số lượng giá trị lẻ trong [0, 1000]\t: {odd}")

people = {"Emma": 71, "Jack": 44, "Amy": 22, "Ben": 12}

# c1: nếu chỉ có 1 người có tuổi lớn nhất
print(max(people, key=people.get))

# c2: nếu có 2 người có tuổi lớn nhất như nhau
for key, value in people.items():
    if value == max(people.values()):
        print(f"Người lớn tuổi nhất {key}: {value}")
