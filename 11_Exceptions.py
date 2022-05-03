# Создайте и выполните функцию с блоком try - except
# обрабатывающим попытку распечатать несуществующую переменную.

def variable_exception():
    try:
        print(a)
    except Exception as e:
        print(f"function variable_exception() \n   Exception: ", e)

# Создайте и выполните функцию перевода списка строк
# в список целых чисел с блоком try - except, обрабатывающим ошибки преобразования.
# В случае ошибки выводить сообщение на экран и
# не добавлять новый элемент в итоговый список.

def show_list():
        string_array = ['test', "2", '12', '15', '7']
        int_array = []
        for elem in string_array:
            try:
                int_array.append(int(elem))
            except Exception as e:
                print(f"function show_list() \n   Exception: ", e)
        print(int_array)

# Создайте и выполните функцию с блоком ry - except - finally,
# обрабатывающим попытку записать строку в файл, открытый на чтение.
# В блоке finally выполнить закрытие файла.

def write_into_file(file):
    f = open(file, "r", encoding='utf-8')
    try:
       f.write("info")
    except Exception as e:
       print(f"function write_into_file() \n   Exception: ", e)
    finally:
       f.close()

def main():
    variable_exception()
    print("----------")
    show_list()
    print("----------")
    write_into_file("additional/11_input.txt")

main()

