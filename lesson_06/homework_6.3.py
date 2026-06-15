#variant 1
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
result = True
lst2 = []
for item in lst1:
    if type(item) == str:
        lst2.append(item)
print(lst2)

# variant 2
lst2 = [num for num in lst1 if type(num) == str]
print(lst2)
