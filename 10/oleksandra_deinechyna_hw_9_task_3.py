# # # # # Задача 3 # # # # #

def methods_amount(arg1):
    def outer(function):
        def wrapper():
            methods: list = function()
            methods_amount: int = len(methods)
            print(f'{arg1}', methods_amount)
        return wrapper
    return outer

@methods_amount('Need to learn')
def methods() -> list:
    user_object: str = input('Enter your Python object: ')
    methods: list = [f for f in dir(user_object) if not f.startswith("__")]
    print(methods)
    return methods

print(methods())

# Не могу понять, откуда все время возникает None в конце при запуске программы?
# Need to learn 45
# None

'''
дописать декоратор, чтобы он принимал аргумент, например текст.
и выводил его тоже.
@methods_amount('need to learn')
[count, index]
'need to learn 2'
2'''