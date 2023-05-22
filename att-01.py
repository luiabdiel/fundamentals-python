age = int(input('how old are you: '))
license = input('type "yes" if you have a driver is license and "no" if you do not: ')

if age >= 18 and license == 'yes':
    print('you can already drive!')
elif age < 18 and license == 'yes':
    print('this driver is license is illegal')
elif age < 18 and license == 'no':
    print('Wait a few more years..')
elif age >= 18 and license == 'no':
    print('You can already get your driver is license!!')

print('finished')
