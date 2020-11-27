# Приём данных
print('----------- Ввод данных ----------')
weight = float(input("Введите вес: ").replace(" ", ""))  # Получаем вес
size = float(input("Введите объём: ").replace(" ", "").replace(",", "."))  # Получаем объем
crate = bool(input("Обрешётка: "))  # Получаем bool обрещетки
print('----------------------------------')

my_order = {
    'weight': weight,
    'size': size,
    'crate': crate,
    'oversize': False,
    'cost': 0,
}
print('------------Input data:-----------'
      '\nВес: ' + str(my_order['weight']) + '\n'
      'Объём: ' + str(my_order['size']) + '\n'
      'Обрешётка: ' + str(my_order['crate']) + '\n'
      'Негабарит: ' + str(my_order['oversize']) + '\n'
      'Стоимость заявки: ' + str(my_order['cost']) + '\n')

# --------------------
# Тарифы и коэффиценты
# --------------------
prices = {
    'weight': {
        'min': 400,
        'max': 4.4
    },
    'size': {
        'min': 200,
        'max': 1160
     },
    'crate': 30,
    'oversize': 30
}
check_oversize = {
    'weight': 250.000,  # кг
    'size': 10.000  # м3
}

# Проверка обрешётки
if my_order['crate']:  # Если выбрана обрещетка, тогда увеличиваем габариты груза на коэффициент
    my_order['weight'] = my_order['weight'] * (1+(prices['crate']/100))
    my_order['size'] = my_order['size'] * (1+(prices['crate']/100))
    # print('\n' + str(my_order))

# Определение способа расчета по весу или объему
if my_order['size'] * 200 <= my_order['weight']:
    print('\nСчитаем по весу')

    if my_order['weight'] <= check_oversize['weight']:
        my_order['cost'] = prices['weight']['min']
        print("Вес: Минимальный тариф")
    else:
        my_order['oversize'] = True
        my_order['cost'] = (my_order['weight']*prices['weight']['max']) * (1+(prices['oversize']/100))
        print("Вес: Максимальный тариф")
else:
    if my_order['size'] <= check_oversize['size']:
        my_order['cost'] = prices['size']['max'] * my_order['size']
        print("Объём: Минимальный тариф")
    else:
        my_order['oversize'] = True
        my_order['cost'] = (my_order['size']*prices['size']['max']) * (1+(prices['oversize']/100))
        print("Объём: Максимальный тариф")

# Итоговая стоимость
print('\nВес: ' + str(my_order['weight']) + '\n'
      'Объём: ' + str(my_order['size']) + '\n'
      'Обрешётка: ' + str(my_order['crate']) + '\n'
      'Негабарит: ' + str(my_order['oversize']) + '\n'
      'Стоимость заявки: ' + str(my_order['cost']) + '\n')
