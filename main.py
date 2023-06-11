import random

n = random.randint(1, 100)
count = 5

print('Добро пожаловать в числовую угадайку. У вас всего 5 попыток, чтобы отгадать число')


def is_valid(x):
    if x.isdigit() and 1 <= int(x) <= 100:
        return True
    else:
        return False

while True:
    x = input('Введите пожалуйста число от 1 до 100: ')
    if count == 1:
        print('Число попыток закончилось. Вы проиграли')
        break
    if is_valid(x):
        if int(x) < n:
            print('Введенное число меньше загаданного. Попробуйте еще раз')
            count -= 1
            print('Число попыток: ', count)
        elif int(x) > n:
            print('Введенное число больше загаданного. Попробуйте еще раз')
            count -= 1
            print('Число попыток: ', count)
        elif int(x) == n:
            print('Вы угадали число!')
            break
    else:
        print('Может всё-таки введете число от 1 до 100?')
        count -= 1
        print('Число попыток: ', count)


print('Спасибо, что сыграли в Угадайку')

