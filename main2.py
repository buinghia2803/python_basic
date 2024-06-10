"""
    list in list
    copy list
    list slicing => new list
"""

# list in list
friends = [['Bob', 23], ['Jen', 45], ['Kne', 68]]

print(type(friends[0]))

print(friends[0][0]) # Bob

# ---------------------

# copy list
lst1 = [1, 3, 2]
lst2 = lst1
print(lst1 is lst2) # is: so sanh ve dia chi bo nho
print(lst1 == lst2) # ==: so sanh gia tri

lst1 = [1, 3, 2]
lst2 = lst1.copy()
# id
print(id(lst1), id(lst2))
print(lst1 is lst2) # is: so sanh ve dia chi bo nho la id
print(lst1 == lst2) # ==: so sanh gia tri

# ------------------------

# list slicing: lay ra 1 phan o list ban dau
# a[start:stop:step] start, stop(ko lay gia tri o stop) la key, step la buoc nhay

a = [1, 3, 10, 100, 45]

new_lst = a[0:2:1] # lay tu key 0 den key 2 (nhung ko lay 2) va buoc nhay la 1
print(new_lst is a)
print(new_lst)

new_lst = a[:2] # viet gon cua cai tren
print(new_lst)

new_lst = a[1:-1] # lay tu key 1 den -1 (o giua)
print(new_lst)

new_lst = a[1:] # lay tu key 1 den het
print(new_lst)

new_lst = a[:] # copy toan bo
print(new_lst)

new_lst = a[::-1] # lat ngc mang (su dung list slicing)
print(new_lst)