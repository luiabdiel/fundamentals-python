temp_f = int(input('Enter the temperature in Fahrenheit: '))


def temp_c(temp):
    return 5 * ((temp - 32) / 9)


conversion = temp_c(temp_f)

print('Temperature in celsius is: {}'.format(conversion))
