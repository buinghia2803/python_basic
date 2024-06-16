"""
    for, while
    break: thoát hoàn toàn ra khỏi vòng lặp chứa nó
    continue: bỏ qua những câu lệnh bên dưới nó và chuyển sang vòng lặp mới
"""

# range(start, stop, step)
# chu y: start, stop, step chi nhan int
r = range(0, 5)
print(r)  # range(0, 5)

lst = list(r)
print(lst)  # [0, 1, 2, 3, 4]

lst = list(range(1, 21))
print(lst)

lst = list(range(1, 21, 2))
print(lst)

lst = list(range(10, 0, -1))
print(lst)

lst = list(range(-4))  # range(0, -4, 1)
print(lst)  # []

# for: lap so vong lap xac dinh
for _ in range(5):
    print("Hello world!")

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

print("-" * 50)

# while: lap so vong lap khong xac dinh
s = input("> ")
while s != "q":
    print("hello")
    s = input("> ")

# for long
for i in range(5):
    for j in range(3):
        print(i, j, sep=" - ")
"""
    0 - 0
    0 - 1
    0 - 2
    1 - 0
    1 - 1
    1 - 2
    2 - 0
    2 - 1
    2 - 2
    3 - 0
    3 - 1
    3 - 2
    4 - 0
    4 - 1
    4 - 2
"""

# break
for i in range(1, 21):
    if i > 5:
        break
    print(i, end=" ")
# => 1 2 3 4 5

# continue
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
# => 1 3 5 7 9 11 13 15 17 19

for i in range(1, 21):
    print(i, end=" ")
else:
    print("Success")

while 1 == 0:
    print("python")
