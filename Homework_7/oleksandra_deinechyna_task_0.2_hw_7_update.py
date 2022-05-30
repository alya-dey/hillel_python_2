''' сделать пример функции без return c pass or ...
сделать 5 различных функций на свое усмотрение. '''

# Функция без return
def lights_on():
    pass


# Пример функции №1
def summing(x, y):
    z = x+y
    return z


print(summing(2, 6))


# Пример функции №2
def count_cost():
    milk_price = int(input('Enter milk price '))
    bread_price = int(input('Enter bread price '))
    egg_price = int(input('Enter eggs price '))
    return f'Cost of all products = {milk_price + bread_price + egg_price}'


print(count_cost())

# Пример функции №3
def upper_letters_into_reversed_list(x):
    x = list(reversed(x.upper()))
    return x


print(upper_letters_into_reversed_list('Hello'))


# Пример функции №4
# Комент "замість отакого краще юзати буль та повертати його :) # а функцію назвати з is_
# Тут не до кінця зрозуміла, як саме краще переробити
def available_products(product):
    products_in_shop = ['milk', 'beer', 'bread', 'tea', 'sugar']
    for i in products_in_shop:
        if i == product:
            return 'Product available'
        return 'Product is not available'


product = input('What product are you interested in?\n')
print(available_products(product))


# Пример функции №5
# Коммент "якщо строки дублюються- можне написати строку один раз а те ще міняється подставляти?)
# бо бачу у вас два рази Number {number}"
# Теж не дуже зрозуміла, як можна ретурн по двом умовам перетворити в одну строку.
def number_test():
    number = input('Enter your integer number to check if it is positive or negative: ')
    if int(number) > 0:
        return f'Number {number} is positive'
    elif int(number) < 0:
        return f'Number {number} is negative'
    elif int(number) == 0:
        return 'You number is zero'


print(number_test())


