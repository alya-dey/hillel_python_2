# # # # # Задача 4 # # # # #

def memo_function(f):
    memo: dict = dict()

    def func(*args: int):
        print(f'Run with {args=}, {memo=}')
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return func

@memo_function
def func(*args: int):
    print(f'Run func with {args=}')
    x = [i**2 for i in args]
    return x


print(func(1, 4, 6), '\n')
print(func(2, 5, 8), '\n')
print(func(9, 3), '\n')


'''
Ваша задача - создать декоратор для функции, которая принимает неограниченное количество позиционных 
ХЕШИРУЕМЫХ элементов.
Декоратор добавляет следующий функционал:
Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть результат выполнения этой функции из 
памяти, а не вычислять его заного.
Если не вызывалась - вычислить результат, положить его в память, и вернуть.
Подсказка - тут вам пригодятся словари.
'''