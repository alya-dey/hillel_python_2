def max_integer_from_2_ints(arg1: int, arg2: int):
    max_from_two = max([arg1, arg2])
    return max_from_two


def max_integer_from_3_ints(arg1: int, arg2: int, arg3: int):
    max_from_two = max_integer_from_2_ints(arg1, arg2)
    max_from_three = max_integer_from_2_ints(max_from_two, arg3)
    return max_from_three


print(max_integer_from_3_ints(5, 14, 18))


'''
Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать 3 аргумента и 
находить максимум с помощью функции1.
в итоге будет .
псевдокод
функция_нахождения_макс_из_2х(арг1, арг2):
return максимальное значение из 2х аргументов
функция_нахождения_макс_из_3х(арг1, арг2, арг3):
использую тут функция_нахождения_макс_из_2х()
return максимальное значение из 3х аргументов.

пример
def finding_max_tw(one, two):
    pass
def finding_max_three(one, two, three):
    middle = finding_max_tw(one, two)
    return finding_max_tw(middle, three)

'''
