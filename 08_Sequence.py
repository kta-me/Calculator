# Напишите программу для вычисления количества продаж и среднего чека в интервалах:
# a. До 1000 р включительно
# b. От 1000 р до 3000 р включительно
# c. От 3000 р до 5000 р включительно
# d. Выше 5000 р.

sales = [2033, 300.50, 1550, 2703, 5110, 2146, 4733, 7114, 1614, 3105, 3155, 853, 10114, 1315]
# sales = [900, 1000, 2000, 4000, 6000]
# sales = [100, 1200, 400, 7000]

def get_info(sales):
    less_1000_count_of_sales = 0
    less_1000_avg_check = 0
    more_1000_and_less_3000_count_of_sales = 0
    more_1000_and_less_3000_avg_check = 0
    more_3000_and_less_5000_count_of_sales = 0
    more_3000_and_less_5000_avg_check = 0
    more_5000_count_of_sales = 0
    more_5000_avg_check = 0

    for sale in sales:
        if sale <= 1000:
            less_1000_count_of_sales += 1
            less_1000_avg_check += sale
        elif sale > 1000 and sale <= 3000:
            more_1000_and_less_3000_count_of_sales += 1
            more_1000_and_less_3000_avg_check += sale
        elif sale > 3000 and sale <= 5000:
            more_3000_and_less_5000_count_of_sales += 1
            more_3000_and_less_5000_avg_check += sale
        else:
            more_5000_count_of_sales += 1
            more_5000_avg_check += sale

    if less_1000_count_of_sales > 0:
        less_1000_avg_check = less_1000_avg_check / less_1000_count_of_sales

    if more_1000_and_less_3000_count_of_sales > 0:
        more_1000_and_less_3000_avg_check = more_1000_and_less_3000_avg_check / more_1000_and_less_3000_count_of_sales

    if more_3000_and_less_5000_count_of_sales > 0:
        more_3000_and_less_5000_avg_check = more_3000_and_less_5000_avg_check / more_3000_and_less_5000_count_of_sales

    if more_5000_count_of_sales > 0:
        more_5000_avg_check = more_5000_avg_check / more_5000_count_of_sales

    print_info("До 1000 руб. включительно: ", less_1000_avg_check, less_1000_count_of_sales)
    print_info("От 1000 руб. до 3000 руб. включительно: ", more_1000_and_less_3000_avg_check, more_1000_and_less_3000_count_of_sales)
    print_info("От 3000 руб. до 5000 руб. включительно", more_3000_and_less_5000_avg_check, more_3000_and_less_5000_count_of_sales)
    print_info("Более 5000 руб.", more_5000_avg_check, more_5000_count_of_sales)

def print_info(title, avg_summ, count):
    print(title)
    print("Количество продаж: " + str(count))
    print("Средний чек: {:.2f}".format(avg_summ) + " руб.")
    print("")

get_info(sales)