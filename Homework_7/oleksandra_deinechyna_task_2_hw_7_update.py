"""написать функцию которая принимает в качестве аргумента номер месяца,
и возвращает строку - время года, этого месяца"""

def season_determining(number_of_month: int):
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
    return season


print(season_determining(12))


def season(month):
    match month:
        case 1 | 2 | 12:
            return "Winter"
        case 3 | 4 | 5:
            return "Spring"
        case 6 | 7 | 8:
            return "Summer"
        case 9 | 10 | 11:
            return "Winter"
        case _:
            return "Error, wrong number of month"




