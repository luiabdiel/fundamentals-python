# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido.
# E continue o pedido até que o usuário informe um valor válido.

while True:
    grade = int(input('Enter a grade from 0 to 10: '))

    if 0 <= grade <= 10:
        print('Valid grade. Congratulations!')
        break
    else:
        print('Invalid grade, please try again.')
