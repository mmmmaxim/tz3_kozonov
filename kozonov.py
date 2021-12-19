import time
import statistics


# Функция нахождения минимума;
def find_min(numbers):
    if numbers:
        minimum = numbers[0]
    else:
        return "No numbers in list found"

    for numb in numbers:
        if numb < minimum:
            minimum = numb

    return minimum


# максимума;
def find_max(numbers):
    if numbers:
        maximum = numbers[0]
    else:
        return "No numbers in list found"

    for numb in numbers:
        if numb > maximum:
            maximum = numb

    return maximum


# суммы;
def find_sum(numbers):
    if numbers:
        res = 0
    else:
        return "No numbers in list found"

    for numb in numbers:
        try:
            res += numb
        except OverflowError:
            return 'inf'

    return res


# произведения.
def find_mult(numbers):
    if numbers:
        res = 1
    else:
        return "No numbers in list found"

    for numb in numbers:
        try:
            res *= numb
        except OverflowError:
            return 'inf'

    return res


# Считывание чисел из файла
def read_file(filename):
    with open(filename, mode="r") as f:
        numbers = []
        for line in f.readlines():
            for numb in line.split():
                numbers.append(float(numb))

    return numbers


def call_all_to_test(file):
    """

    Выполним все функции для того, чтобы в дальнейшем узнать время их исполнения
    Функции передается имя файла
    Функция ничего не возвращает
    """
    file = read_file(file)
    find_min(file)
    find_max(file)
    find_sum(file)
    find_mult(file)
    find_sum_odd_negative_number(file)


def check_called(name, number):
    checks = []
    if isinstance(number, int):
        if number > 0:
            start = time.time()
            call_all_to_test(name)
            finish = time.time()
            checks.append(finish - start)
        checks_sum, checks_number = sum(checks), len(checks)
        return checks_sum / checks_number
    return None


def find_sum_odd_negative_number(array):
    """
    Найти моду в списке
    В функцию передается список чисел
    Функция возвращает моду списка (если их несколько, вернет самую первую из них)
    Если список пустой, функция вернет None
    """

    if not array:
        return None

    res = 0

    for numb in array:
        if numb % 2 != 0:
            if numb < 0:
                res += numb

    return res
