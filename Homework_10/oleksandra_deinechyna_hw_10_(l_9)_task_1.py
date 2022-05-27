# all()
list1 = [True, True, True]
print('list1 =', all(list1))
list2 = [True, False, True]
print('list2 =', all(list2))
list3 = []
print('list3 =', all(list3))
list4 = [1, 16, 'Hello', True]
print('list4 =', all(list4))
list5 = [5, '', [], 18]
print('list5 =', all(list5))
str1 = 'Hello'
print('str1 =', all(str1))

# any()
list6 = [True, False, True]
print('list2 =', any(list2))
list7 = []
print('list3 =', any(list3))
list8 = [5, '', [], 18]
print('list5 =', any(list5))

# filter()
# 1) Отфильтровывает четные числа в списке:
numbers = list(range(1, 11))
def filter_numbers(x):
    if x % 2 == 0:
        return True
    return False
numbers2 = filter(filter_numbers, numbers)
print(list(numbers2))

# 2) Отфильтровывает только True значения, вместо функции указываем None:
list9 = [0, None, True, False, [], 15, 'Hello']
print(list(filter(None, list9)))

# 3) Фильтр для удаления стоп-слов в тексте:
list_of_bad_words = ['черт', 'чёрт', 'Черт', 'ЧЕРТ']
some_text = 'Черт бы тебя побрал, ты чертополох!'
text_by_words = some_text.split()
filtered_text = ' '.join(filter(lambda x: x not in list_of_bad_words, text_by_words))
print(filtered_text)


'''
зробити по 3 приклади функцій all(), any() та  filter()
'''