print("----- № 1 -----")
for i in range(10, 20):
    print(i, end=' ')
print("")
print("----- № 2 -----")
for i in range(10, 20):
    if i%3 != 0:
        continue
    print(i, end=' ')
    print("")
print("----- № 3 -----")
numbers = [2, 3, 0.5, 15, 7, 11, 12, 7, 11, 16]
for number in numbers:
    if number < 1:
        print(number)
        break
    else:
        print("Элемент не найден")