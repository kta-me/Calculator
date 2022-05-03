print("----- № 1 -----")
def function_5(numbers):
    for number in numbers:
        if number%5 == 0:
            print(number)

numbers = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
function_5(numbers)

print("----- № 2 -----")
def min_function(numbers):
    for number in numbers:
        a = number
        if a < number:
            a = number
    return a
print(min_function(numbers))

print("----- № 3 -----")
my_value = 10
numbers = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def find_function(numbers):
    for number in numbers:
        if number < my_value:
            return number
    return "Не найдено"

print(find_function(numbers))