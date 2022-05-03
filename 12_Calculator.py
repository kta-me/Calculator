import tkinter as tk

window = tk.Tk()
window.geometry("300x200")
window.title("Python калькулятор")

first_number_label = tk.Label(text = "Первое число:")
first_number_label.grid(column = 0, row = 0, padx = 10, pady = 10)
second_number_label = tk.Label(text = "Второе число:")
second_number_label.grid(column = 0, row = 1)
result_number_label = tk.Label(text = "Итого:")
result_number_label.grid(column = 0, row = 2, sticky="W", padx = 10, pady = 10)

first_number = tk.Entry()
first_number.grid(column = 1, row = 0)
second_number = tk.Entry()
second_number.grid(column = 1, row = 1)
result_number = tk.Label(text = "")
result_number.grid(column = 1, row = 2, sticky="W")

def get_result():
    number_first = int(first_number.get())
    number_second = int(second_number.get())
    result_number['text'] = number_first * number_second

button = tk.Button(window, text = "Умножить", command = get_result)
button.grid(column = 1, row = 3)

window.mainloop()