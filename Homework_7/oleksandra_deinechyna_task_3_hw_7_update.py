'''
написать функцию, которая принимает в качестве аргументов два списка, а возвращает список,
состоящий из элементов этих двух списков, при чем первый элемент списка - первый элемент первого аргумента,
второй элемент списка - первый элемент второго списка, третий элемент - второй элемент первого списка,
четвертый - второй элемент второго аргумента и т.д.
т.е для аргументов [1, 2, 3] и [11, 22, 33] функция должна вернуть [1, 11, 2, 22, 3, 33].
Будет плюсом использование генераторов последовательностей для решения этой задачи.
'''

def merging_lists(list1, list2):
    # Сначала сшиваем 2 списка через функцию zip, получится список кортежей:
    merged_list_of_tuples = list(zip(list1, list2))
    # Потом превращаем список кортежей в список:
    merged_list = []
    for x, y in merged_list_of_tuples:
        merged_list.append(x)
        merged_list.append(y)
    return merged_list


print(merging_lists([1, 2, 3], [11, 22, 33]))


# Через генератор послідовностей
def merging_lists2(list1, list2):
    result = [item for sublist in zip(list1, list2) for item in sublist]
    return result


print(merging_lists2([1, 2, 3], [11, 22, 33]))


# І такий варіант:
# merged_list = [i for j in merged_list_of_tuples for i in j]






