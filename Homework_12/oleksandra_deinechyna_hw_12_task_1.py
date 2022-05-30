"""Задача 1 10 баллов написать 3 примера генераторных функций с различными последовательностями."""

# Пример 1: вывести списоок продуктов построчно:
list_of_products = ['milk', 'cheese', 'coffee', 'beer', 'bread']
def list_items():
    for item in list_of_products:
        yield item

example1 = list_items()
for i in example1:
    print(i)

# Пример 2: посчитать среднее арифметическое последовательностей (от 1 до 10, 2 до 10 и т.д.)
def get_list():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len (a)

example2 = get_list()
print(list(example2))

# Пример 3. Факториалы каждого элемента последовательности
def factorial(n):
    p = 1
    for i in range(1, n+1):
        p = p * i
        yield p

example3 = factorial(10)
print(list(example3))