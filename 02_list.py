# time complexity O(n) or O(1)

# -------------------


#          0  1   2   3  4
#         -5 -4  -3  -2 -1
numbers = [1, 2, 3.5, 4, 1]

print(numbers[1])  # 2
print(numbers[-1])  # 4

numbers.append(100)
print(numbers)

numbers.remove(1)  # xoa phan tu co gia tri la 1 dau tien trong list

last_value = numbers.pop()
print(last_value)  # lay ra ptu xoa
print(numbers)  # xoa phan tu cuoi cung trong list

numbers.extend([2.5, 1000, 100])  # them cac phan tu nay vao cuoi list
print(numbers)

numbers[0] = 75  # gan ptu o key 0 thanh 75
print(numbers)

amount = numbers.count(1)  # 2 (dem 1 ptu nao do trong list)
print(amount)

numbers.clear()  # []
print(numbers)

amount = len(numbers)
print(amount)

numbers = [1, 2, 3.5, 4, 1]

# insert
numbers.insert(0, 1000)
print(numbers)

# index
index_of_3p5 = numbers.index(3.5)
print(index_of_3p5)

# reverse
numbers.reverse()  # lat ngc list
print(numbers)

# sort
numbers.sort()  # sap xep tang dan
print(numbers)

numbers.sort(reverse=True)  # sap xep giam dan
print(numbers)

friends = ["jack", "nghia"]
del friends[1]  # xoa phan tu key la 1
print(friends)

# ------------------
numbers = [12, 34, 56, -100, 67]
max_value = max(numbers)
print(max_value)

min_value = min(numbers)
print(min_value)
