"""
    + Advanced Set
    + Dictionary: key: value
    + sum, len, min, max, join
"""

set1 = {1, 4, 3, 2}
set2 = {2, 3, 10, -10}
set3 = {10, 11, 20}

set3 = set1.intersection(set2)  # phần chung (giao)
print(set3)
print(set1 & set2)  # phần chung (giao)

set3 = set1.difference(set2)
# nam trong set1 ko nam set2 va ngc lai, chu y: neu dung ham thi trong ngoac co the la set list tuple
print(set3)
print(set1 - set2)  # chu y: dung toan tu thi ca 2 phai la set

set4 = set1.union(set2).union(set3)  # lay het
print(set4)
print(set1 | set2 | set3)  # pipe

set3 = set1.symmetric_difference(set2)  # lay tat ca nhung tru phan chung
print(set3)
print(set1 ^ set2)

print("-" * 50)

import json

student = {
    "name": "Bob",
    "age": 23,
    "grades": [45, 67, 90, 98, 99],
}

print(json.dumps(student, indent=4))

value = student["name"]
print(value)

value = student.get("id", "SV001")
print(value)

student["id"] = "SV001"
student["name"] = "Jack"
print(student)

# them key va value
# c1
student.update(id="SV001", gender="male")
print(json.dumps(student, indent=4))

# c2
info = {"id": "SV001", "gender": "male"}
student.update(info)
print(json.dumps(student, indent=4))

# c3
info = [("id", "SV001"), ("gender", "male")]
student.update(info)
print(json.dumps(student, indent=4))

# remove
# c1
value = student.pop("name")
print(value)

print(json.dumps(student, indent=4))

# c2
# del student["name"]
# print(json.dumps(student, indent=4))

tup = student.popitem()  # xoa key value cuoi cung, gia tri xoa la 1 tup
print(tup)

print(json.dumps(student, indent=4))

# keys
keys = list(student)
print(keys)

# values
values = list(student.values())
print(values)

# bien Dictionary thanh tup
items = list(student.items())
print(items)

# clear
student.clear()
print(student)  # {}: la Dictionary

print("-" * 50)

lst = []  # sum [] la 0
lst = [1, 2, 3, 4]

total = sum(lst, 10)
print(total)

lst = [[1, 2, 3, 4], [10, 20, -10]]

total = sum(lst, [0])
print(total)

lst = []  # len [] la 0
lst = ["a", "b", "c", "f"]
print(len(lst))

lst = []  # min [] la ra loi
# print(min(lst))

lst = []  # max [] la ra loi
# print(max(lst))

lst = ["4", "2", 3, 1]
s = " - ".join(map(str, lst))

print(s)
