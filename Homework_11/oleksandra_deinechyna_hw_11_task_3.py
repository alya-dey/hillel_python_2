"""Задача 3.  20 баллов Написать функцию которая принимает от пользователя 2 аргумента и делит один на другой.
при попытке деления на ноль вывести пользователю "ай яй яй делить на ноль можно не многим"
Все остальные исключения с поймать и вывести их значение в текстовом формате.
И в любом случае вывести. " I 'am happy that you learn python"""


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Ай яй яй делить на ноль можно не многим"
    except Exception as i:
        return f"Ошибочка вышла: {i}"
    else:
        return f"Result is {result}"
    finally:
        print("I am happy that you learn python")


print(divide(4, 2))
