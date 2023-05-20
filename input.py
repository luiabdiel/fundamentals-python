import datetime

name = input('What your name? ')
birth_year = int(input('When were you born? '))

current_year = datetime.datetime.now().year
age = current_year - birth_year

print(f'{name}, you have {age} years right?')
