import kozonov
import functools
import statistics


names_w_arrays = {
    "check.txt": kozonov.read_file("check.txt"),
    "check2.txt": kozonov.read_file("check2.txt"),
    "check3.txt": kozonov.read_file("check3.txt"),
    "check4.txt": kozonov.read_file("check4.txt"),
    "check5.txt": kozonov.read_file("check5.txt"),
    "check6.txt": kozonov.read_file("check6.txt"),
    "check7.txt": kozonov.read_file("check7.txt"),
}

def test_minimum_search():
    """Протестриуем функцию нахождения минимума для каждого списка"""
    for array in names_w_arrays.values():
        assert min(array) == kozonov.find_min(array)

def test_maximum_search():
    """Протестриуем функцию нахождения максимума для каждого списка"""
    for array in names_w_arrays.values():
        assert max(array) == kozonov.find_max(array)

def test_sum_get():
    """Протестриуем функцию нахождения суммы для каждого списка"""
    for array in names_w_arrays.values():
        assert sum(array) == kozonov.find_sum(array)

def test_prod_get():
    """Протестриуем функцию нахождения произведения для каждого списка"""
    for array in names_w_arrays.values():
        assert functools.reduce((lambda x, y: x * y), array) == kozonov.find_mult(array)

def test_search_mode():
    """Протестируем функцию нахождения медианных значений"""
    for array in names_w_arrays.values():
        if array:
            assert sum([x for x in array if x < 0 and x % 2 != 0]) == kozonov.find_sum_odd_negative_number(array)
            continue
        assert None is kozonov.find_sum_odd_negative_number(array)

def test_check_called_time():
    """Протестируем, как минимальное время исполнения растет с ростом размера файла"""
    for name, array in names_w_arrays.items():
        print(f"Для файла {name} минимальное время исполнения за 30 попыток составило"
              f"{kozonov.check_called(name, 1)}.")
