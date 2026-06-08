alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where —— " said Alice.\n"Then it doesn\'t matter which way you go," said '
                       'the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Black sea area: {black_sea_area} ")
print(f"Azov sea area: {azov_sea_area} ")
print(f"Total area: {total_area} ")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# Загальна кількість товарів
total_products = 375291
warehouse_1_2 = 250449  # перший + другий
warehouse_2_3 = 222950  # другий + третій
# Знаходимо кожен склад
warehouse_3 = total_products - warehouse_1_2
warehouse_1 = total_products - warehouse_2_3
warehouse_2 = warehouse_1_2 - warehouse_1
print(f"Warehouse 1: {warehouse_1} products")
print(f"Warehouse 2: {warehouse_2} products")
print(f"Warehouse 3: {warehouse_3} products")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
months = 18
computer_price = monthly_payment * months
print(f"Computer price: {computer_price} UAH")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("remainder after division:")
print("8019 : 8 -> 8019 % 8 =", (8019 % 8 ))
print("9907 : 9 -> 9907 % 9 =", (9907 % 9 ))
print("2789 : 5 -> 2789 % 5 =", (2789 % 5 ))
print("7248 : 6 -> 7248 % 6 =", (7248 % 6))
print("7128 : 5 -> 7128 % 5 =",(7128 % 5))
print("19224 : 9 -> 19224 % 9 =", (19224 % 9))

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
order_list = '''List of orders:
- pizza big: 4
- pizza middle: 2
- juice: 4
- cake: 1
- water: 3
'''
pizza_big = 4 * 274
pizza_middle = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_cost = pizza_big + pizza_middle + juice + cake + water
print(order_list)
print("Total cost = pizza_big + pizza_middle + juice + cake + water =", total_cost, "UAH")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
one_page_photos_max = 8
pages_needed = total_photos // one_page_photos_max
remainder = total_photos % one_page_photos_max
if remainder > 0:
    pages_needed += 1
print(f"Total pages needed = {pages_needed}")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
tank_volume = 48
gasoline_consumption = 9 # for 100 km

# Скільки літрів бензину знадобиться для такої подорожі
total_gasoline = distance // 100 * gasoline_consumption
print(f"Total gasoline = {total_gasoline} liters")

# Скільки разів заправлятись
refueling = total_gasoline // tank_volume
remainder = total_gasoline % tank_volume
if remainder > 0:
    refueling += 1
print(f"Refueling = {refueling}")
