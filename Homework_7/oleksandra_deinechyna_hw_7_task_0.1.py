# 1) List comprehension
my_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list1: list = [i**2 for i in my_list]
print(my_list1)
my_list2: list = [i + 1 for i in my_list]
print(my_list2)
my_list3: list = [i*i for i in my_list if i % 2 == 0]
print(my_list3)
my_list_str: list = ['one', 'two', 'three', 'four', 5]
my_list4: list = [i+'tap' for i in my_list_str if isinstance(i, str)]
print(my_list4)
my_list5: list = [i*2 for i in my_list_str]
print(my_list5)

# 2) Dict comprehension
dict_of_squares = {i: i**2 for i in range(1,11)}
print(dict_of_squares)
my_dict: dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
my_dict_up = {key: value.upper() for key, value in my_dict.items()}
print(my_dict_up)
my_dict3 = {key*2: value + '+' + value for key, value in my_dict.items()}
print(my_dict3)
phrase: str = 'Please count letters in this sentence'
my_dict4 = {key: phrase.count(key) for key in phrase}
print(my_dict4)
my_dict5 = {key: value.lower() for key, value in my_dict_up.items() if key % 2 == 0}
print(my_dict5)

# 3) Set comprehension
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set1 = {i+2*i for i in my_set}
print(my_set1)
my_set2 = {i**2 for i in my_set if i % 3 == 0}
print(my_set2)
my_set3 = {str(i) for i in my_set}
print(my_set3)
my_set4 = {i+' Mississippi' for i in my_set3}
print(my_set4)
my_set5 = {i-1 for i in my_set}
print(my_set5)

'''
1) 5 примеров list comprehension
2) 5 examples with DICT comprehension
3) 5 примеров с set comprehensions
'''
