import random

chars = 'abcdefghikl'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password = ''
    for i in range(length):
        password += random.choise(chars)
    print(password)
