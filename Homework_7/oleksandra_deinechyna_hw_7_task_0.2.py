# Функция без return
def lights_on():
    pass

# Пример функции №1
def summing(x, y):
    z = x+y
    return print(z)

summing(2, 6)

# # Пример функции №2
# def count_cost():
#     milk_price = int(input('Enter milk price '))
#     bread_price = int(input('Enter bread price '))
#     egg_price = int(input('Enter eggs price '))
#     return print('Cost of all products = ' + str(milk_price + bread_price + egg_price))
#
# count_cost()
#
# # Пример функции №3
# def upper_letters_into_reversed_list(x):
#     x = list(reversed(x.upper()))
#     return print(x)
#
# upper_letters_into_reversed_list('Hello')
#
# # Пример функции №4
# def available_products(product):
#     products_in_shop = ['milk', 'beer', 'bread', 'tea', 'sugar']
#     for i in products_in_shop:
#         if i == product:
#             return 'Product available'
#         return 'Product is not available'
#
# product = input('What product are you interested in?\n')
# print(available_products(product))

# Пример функции №5
def number_test():
    number = input('Enter your integer number to check if it is positive or negative: ')
    if int(number) > 0:
        print(f'Number {number} is positive'.format(number))
    elif int(number) < 0:
        print(f'Number {number} is negative'.format(number))
    elif int(number) == 0:
        print('You number is zero')

number_test()

'''
сделать пример функции
без return c pass or ...
сделать 5 различных функций на свое усмотрение.
'''
