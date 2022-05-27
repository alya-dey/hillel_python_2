list_of_products = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
# Можем указать анонимную функцию в качестве ключа для сортировки:
list_of_products.sort(key=lambda x: (x[1]))
print(list_of_products)

'''
Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.
Пример(Example)
Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]
'''
