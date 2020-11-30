from prices import *
from my_decorator import time_calc

# Приём данных
print('----------- Ввод данных ----------')
weight = float(input("Введите вес: ").replace(" ", ""))  # Получаем вес
size = float(input("Введите объём: ").replace(" ", "").replace(",", "."))  # Получаем объем
crate = bool(input("Обрешётка: "))  # Получаем bool обрещетки

my_order = {
    'weight': weight,
    'size': size,
    'crate': crate,
    'oversize': False,
    'cost': 0,
}


@time_calc
def my_calc():

    print('------------Input data:-----------')
    print('Вес: ' + str(my_order['weight']))
    print('Объём: ' + str(my_order['size']))
    print('Обрешётка: ' + str(my_order['crate']))
    print('Негабарит: ' + str(my_order['oversize']))
    print('Стоимость заявки: ' + str(my_order['cost']))

    # Проверка обрешётки
    if my_order['crate']:  # Если выбрана обрещетка, тогда увеличиваем габариты груза на коэффициент
        my_order['weight'] = my_order['weight'] * (1 + (prices['crate'] / 100))
        my_order['size'] = my_order['size'] * (1 + (prices['crate'] / 100))
        # print('\n' + str(my_order))

    # Определение способа расчета по весу или объему
    if my_order['size'] * 200 <= my_order['weight']:
        if my_order['weight'] <= check_oversize['weight']:
            my_order['cost'] = prices['weight']['min']
            print("Вес: Минимальный тариф")
        else:
            my_order['oversize'] = True
            my_order['cost'] = (my_order['weight'] * prices['weight']['max']) * (1 + (prices['oversize'] / 100))
            print("Вес: Максимальный тариф")
    else:
        if my_order['size'] <= check_oversize['size']:
            my_order['cost'] = prices['size']['max'] * my_order['size']
            print("Объём: Минимальный тариф")
        else:
            my_order['oversize'] = True
            my_order['cost'] = (my_order['size'] * prices['size']['max']) * (1 + (prices['oversize'] / 100))
            print("Объём: Максимальный тариф")

    # Итоговая стоимость
    print('---------- Output data -----------'
          '\nВес: ' + str(my_order['weight']),
          '\nОбъём: ' + str(my_order['size']),
          '\nОбрешётка: ' + str(my_order['crate']),
          '\nНегабарит: ' + str(my_order['oversize']),
          '\nСтоимость заявки: ' + str(my_order['cost']) + '\n')


my_calc()
