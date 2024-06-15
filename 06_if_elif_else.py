"""
    if-elif-else
"""

if 1 > 0:
    print("1 > 0")
else:
    print("1 <= 0")

n = int(input("n = "))

if n > 0:
    print("So duong")
elif n < 0:
    print("So am")
else:
    print("So 0")

if n % 3 == 0:
    print("n chia het cho 3")
else:
    print("n ko chia het cho 3")

print("n chia het cho 3" if n % 3 == 0 else "n ko chia het cho 3")

a = int(input("a = "))
b = int(input("b = "))

# c1
if a > b:
    print(a)
else:
    print(b)

print(a if a > b else b)

# c2
m = a

if b > a:
    m = b

print(m)

a, b = map(int, input().split())  # split la dung nh` or 1 dau cach de chia thanh mang
print(a if a < b else b)

# eval: danh gia bieu thuc trong chuoi
print(eval("1 + 2"))

lst = list(map(eval, input().split()))
print(lst)

lst = [1, 2, 3, 4]
print(*lst)  # 1 2 3 4
# giong
print(1, 2, 3, 4)
print(*lst, sep=" % ")

x = 2.4567
print(format(x, ".2f"))  # 2.46

print(round(x))  # 2, ra gia tri so nguyen gan nhat x = 3.546 thi se ra 4
print(round(x, 2))  # 2.46

# pow
print(pow(2, 3))  # 8 = 2 ^ 3

# sorted => new list duoc sap xep
lst = [4, 3, 2, 10]
new_lst = sorted(lst, reverse=True)
print(new_lst)

# ord - chr
char = "a"
print("ASCII Code:", ord(char))

ascii_code = 97
print(chr(ascii_code))  # a

# list
s = "abcd"
print(list(s))  # ['a', 'b', 'c', 'd']

lst = list(map(eval, input().split()))
print(lst)

# divmod
print(divmod(4, 3))  # tra ve 1 tuple cua (4 // 3, 4 % 3) => (1, 1): (thuong, du)

thuong, phan_du = divmod(11, 3)  # 11 // 3 = 3, 11 % 3 = 2
print(thuong, phan_du)

# bin
int_number = 10
binary_string = bin(int_number)
print(binary_string)  # 0b1010
"""
    012345
    0b1010
"""
print(binary_string[2:])  # 1010
# giong
print(format(int_number, "b"))  # 1010
print(f"{int_number:b}")  # 1010

# range
print(list(range(256)))
