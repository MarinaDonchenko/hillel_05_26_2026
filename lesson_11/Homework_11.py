data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def get_sum(item):
    numbers = item.split(",")
    sum_ = 0
    try:
        for number in numbers:
            sum_ += int(number)
    except ValueError:
        print("Не можу це зробити!")
        return
    return sum_

for item in data:
    result = get_sum(item)
    if result is not None:
        print(result)