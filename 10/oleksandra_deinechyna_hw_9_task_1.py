# # # # # Задача 1. Замыкания # # # # #

def add_country_code():
    user_number: str = '4307123'
    def inner(country_code: str):
        return country_code + user_number
    return inner

print(add_country_code()('+38044'))



'''
Задача 1. 10 баллов
Написать функцию которая будет добовлять код страны
к номеру телефона с помощью замыкания
внешний вид вызова функции.
my_number = user_telephone('+044')
my_number('838372893')
+044838372893 результат.'''