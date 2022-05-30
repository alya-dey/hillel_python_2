"""
Написать функцию которая принимает в качестве аргумента строку, и возвращает True,
если строка является полиндромом и False если нет.
"""

def is_palindrome(string):
  return string == string[::-1]


print(is_palindrome('atmta'))

# Вище був спрощений варінт цього:
# def is_palindrome(string):
#     # Проверяем, совпадает ли строка и та же строка в обратном порядке:
#     if str(string) == str(string)[::-1]:
#         return True
#     return False


# Вариант 2, длиннее и страннее: если длина строки 1 или 0, єто всегда будет палиндром.
# Если строка длиннее, то проверяем, равны ли первый и последний элемент последовательности.
# И потом через вложение этой же функции внутрь функции сравниваем второй элемент с перепоследним и т.д.
def is_palindrome2(string2):
    if len(string2) <= 1:
        return True
    else:
        return string2[0] == string2[-1] and is_palindrome2(string2[1:-1])


print(is_palindrome2('atmamta'))

