# # # # # Задача 2 # # # # #

def counting_methods_amount(function):
    def wrapper():
        methods: list = function()
        methods_amount: int = len(methods)
        return methods_amount
    return wrapper

@counting_methods_amount
def methods():
    user_object: str = input('Enter your Python object: ')
    methods: list = [f for f in dir(user_object) if not f.startswith("__")]
    print(methods)
    return methods

print(methods())

# Также, как и в дз 5, з. 4, не сообразила, как пользователь может ввести тип обьекта, а не только строку.
# Чтобы работало, как в том дз, надо вместо инпута вводить сразу нужный тип объекта.


'''
Написать функцию которая будет у пользователя брать python обект в любом виде и выводить все его не магические методы 
в списке. и написать декторатор который будет выводить колличество методов в объекте.
Похожую задачу мы уже решали. Можете взять решение из предыдущей . Но декоратор уже ваш полностью)
func(tuple())
[count, index]
@methods_amount
[count, index]
2'''