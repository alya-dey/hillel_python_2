from datetime import date

now = date.today()
year = lambda x: f'Today is {x.year} year,'
month = lambda x: f'of {x.month} month'
day = lambda x: f'{x.day} day'

print(year(now), day(now), month(now))
print(r'Link for datetime documentation: https://docs.python.org/3/library/datetime.html')



'''
познакомиться с модулем datetime и написать программу с помощью lambda для возвращение текущего года, месяца , дня
например результат должен быть таким
import datetime
now = datetime.datetime.now()
.....ваш код))
print(year(now))
print(month(now))
print(day(now))
скинуть мне ссылку на документациюю по datetime.

'''
