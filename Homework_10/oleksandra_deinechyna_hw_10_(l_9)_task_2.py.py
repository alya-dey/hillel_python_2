# 1) Рекурсия вывода чисел с обратным порядком:
def recursive(number):
    print(number)
    if number < 5:
        recursive(number+1)
    print(number)
recursive(1)

# 2) Пример из предыдущего дз ))
def is_palindrome2(string2):
    if len(string2) <= 1:
        return True
    else:
        return string2[0] == string2[-1] and is_palindrome2(string2[1:-1])
print(is_palindrome2('atmamta'))

# 3) Факториал
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

print('''Рекурсія – це спосіб організації циклічного процесу шляхом виклику рекурсивної функції.
Рекурсивна функція – це функція, яка містить код виклику самої себе з метою організації
циклічного процесу. ''')



'''
Зробити 3 приклади Рекурсії. 
Написати формулювання значення Рекурсія.
'''