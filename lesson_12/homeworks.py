#from homework_07
def sum_of_digits(digit1, digit2):
    result = digit1 + digit2
    if float(result).is_integer():
        return int(result)
    return result

#from homework_07
def average_of_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

#from homework_07
def func_max_word(source_text):

    if len(source_text) == 0:
        return 0
    max_len = len(max(source_text, key=len))
    return [word for word in source_text if len(word) == max_len]

#from homework_11
def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    return age