from time import perf_counter


def time_calc(func):
    def wrapper():
        start = perf_counter()
        func()
        end = perf_counter()
        print('Время выполнения скрипта: ' + str(round(end - start, 4)))
    return wrapper
