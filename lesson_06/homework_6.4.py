#variant 1
import random
my_numbers = [random.randint(1, 100) for _ in range(50)]
list_comprehended = [num for num in my_numbers if num%2 == 0]
print(list_comprehended)
print(f"sum of even numbers: {sum(list_comprehended)}")

#variant 2
even_list = []
for num in my_numbers:
    if num %2 == 0:
        even_list.append(num)
print(even_list)
print(f"sum of even numbers: {sum(even_list)}")