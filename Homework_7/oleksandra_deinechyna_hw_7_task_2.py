def season_determining(number_of_month):
    if number_of_month in [1, 2, 12]:
        season = 'Winter'
    elif number_of_month in [3, 4, 5]:
        season = 'Spring'
    elif number_of_month in [6, 7, 8]:
        season = 'Summer'
    elif number_of_month in [9, 10, 11]:
        season = 'Autumn'
    else:
        season = 'Error'
    return print(season)


season_determining(12)


'''
написать функцию которая принимает в качестве аргумента номер месяца, в возвращает строку - время года, этого месяца
'''
