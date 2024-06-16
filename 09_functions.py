"""
    Python functions
"""

def my_func(msg):
    print(msg)

my_func("Hello")

# chú ý: những tham số mặc định phải để ở cuối
def show_full_name(fname, lname="world!"):
    print(f"{fname} {lname}")

show_full_name("Hello", "world!")

def get_full_name(fname, lname="world!"):
    if fname:
        return f"{fname} {lname}"

    return f"Hi {"world!"}"

full_name = get_full_name(lname="world!", fname="Hello")
print(full_name)

def add(x, y=40):
    return x + y

print(add(y=10, x=100))

# không nên dùng
def func(lst=[]): # tránh việc truy vào những kiểu có thể thay đổi được như list và disungnery
    lst.append(2)
    print(lst)

func()
func()

friends = ["Kenny", "Bob", "Jen"]

def my_func():
    f = friends + ["Joe"] # chú ý: code sẽ thực hiện bên phải trước rồi mới gán cho bên trái
    print(f)

my_func()

print((lambda x, y: x + y)(1, 2))

add = lambda x, y: x + y

print(add(1, 2))

print((lambda name: f"Hello, {name}")('name'))

_name = lambda name: f"Hello, {name}"
print(_name('name'))

def greet(msg):
    print("Hello " + msg)
    return None

hello = greet
print(hello("Jen"))

def func():
    pass

# *args
#c1
def add(x, y, z, t):
    return x + y + z + t

print(add(1, 2, 3, 4))

#c2
def add(*args): # 1 dấu *: tập hợp tất cả đối số vị trí
    print(type(args))
    print(args)
    return sum(args)

print(add(1, 2, 3, 4))

lst = [4, 3, 2, 1]
print(*lst)

first, *mid, last = lst
print(first, mid, last)

def add(*lst, operation):
    return operation(lst)

print(add(1, 2, 3, 4, operation=sum))

# ko nên nhân list với số vì sẽ tạo ra 5 cái tham chiếu nếu thay đổi 1 sẽ ảnh hưởng tất cả các còn lại
# lst = [[]] * 5
# lst[1].append(2)
# print(lst)

lst = [[] for _ in range(5)]
lst[1].append(2)
print(lst)

# ví dụ:
print('-'*50)

lst = list(range(10))

# break thoát khỏi vòng lặp chứa nó, chú ý: là thoát hẳn cả else luôn
# khi for không vào if là không bị break thì sẽ vào else
for x in lst:
    if x > 4:
        break
    print(x)
else:
    print('end')

# không được dùng vừa for vừa xóa vì sẽ bị sai index
# lst = ['a', 'b', 'c', 'a', 'a', 'd']

# for x in lst:
#     if x == 'a':
#         lst.remove(x)

# print(lst)

def delete():
    global lst
    lst = [x for x in lst if x != 'a']
    # cái lst mới này vẫn là cái lst cũ tại cùng vị trí trong bộ nhớ

lst = ['a', 'b', 'c', 'a', 'a', 'd']
delete()
print(lst)
