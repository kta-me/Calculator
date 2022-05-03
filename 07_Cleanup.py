### 1
print("--------- № 1 ---------")
def while_fuction(i):
    while i < 3:
        print(i)
        i += 1

while_fuction(1)

### 2
print("--------- № 2 ---------")

a = 22
b = 22
def is_equal(a, b):
    if a == b:
        print("Переменные равны")
    else:
        print("Переменные не равны")

is_equal(a, b)

### 3
print("--------- № 3 ---------")

is_sql_connection = False

def check_sql_connection(is_sql_connection):
    if is_sql_connection:
        print("Есть соединение")
    else:
        print("Соединение отсутствует")

check_sql_connection(is_sql_connection)

### 4
print("--------- № 4 ---------")

summ = 0

def get_summ(summ):
    for i in range(5):
        summ += i
    return summ

print(get_summ(summ))

### 5
print("--------- № 5 ---------")

def function_2(a):
    if a % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")

function_2(9)
function_2(10)
