"""Задача 3 30 баллов: написать функцию которая с помощью assert будет тестировать ваш самописный reduce"""


def my_reduce(func, sequence):
    result = sequence[0]
    for item in sequence[1:]:
        result = func(result, item)
    return result


print(my_reduce(lambda x, y: x+y, [3, 7, 10]))


def test_function():
    assert my_reduce(lambda x, y: x+y, [3, 7, 10]) == 20


print(test_function())