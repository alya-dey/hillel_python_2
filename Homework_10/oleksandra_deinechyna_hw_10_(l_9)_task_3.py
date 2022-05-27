# Декоратор
def decorator1(function):
    def wrapper():
        function()
        print('By the way, you are awesome!')
    return wrapper()

# 1) Пример использования через @
@decorator1
def some_text_function():
    print('1.Welcome to our site.')


# 2) Пример использования через вызов функции:
def some_text_function2():
    print('2.Hello!')
some_text_function2 = decorator1(some_text_function2)

# 3 Декоратор, чтобы красиво обрамить текст )
def decorator2(function):
    def wrapper():
        print('*' * 31)
        function()
        print('*' * 31)
    return wrapper()

@decorator2
def some_text_function3():
    print(':) :) :) *** hElLo *** :) :) :)')


print('''Декоратор — это функция, которая позволяет обернуть другую функцию для 
расширения её функциональности без непосредственного изменения её кода.''')



'''
Зробити 3 прилкади декоратора. 
Написати формулювання значення Декоратор.
'''