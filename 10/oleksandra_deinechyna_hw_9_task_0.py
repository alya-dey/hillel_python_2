# # # # # Задача 0. Замыкания # # # # #

def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
    return inner

o = one()
print(o(), '\n')

o.__closure__
o.__closure__[0]
a = o.__closure__[0].cell_contents
print(a)
print(id(a), '\n')

# Замыкание это функция вместе с привязанной к ней совокупности данных.
# Замыкание это функция внутри которой есть ссылки на переменные, которые были обьявлены вне ее тела.

a.append('asdf')
print(o(), '\n')
