print("№ 1")
a = 10
b = 20

if a == b:
    print("Переменные равны")
elif a > b:
    print(a, " > ", b)
elif a < b:
    print(a, " < ", b)
else:
    print("Конец сравнения")
print("-----------------------")
print("№ 2")
c = 30

if c%3 == 0:
    print(c, " делится на 3")
else:
    print(c, " не делится на 3")
print("-----------------------")
print("№ 3")
d = True
e = False

if d and e:
    print("Обе переменные равно true")
elif d or e:
    print("Одна из переменных равна true")
else:
    print("Ни одна переменная не равна true")
