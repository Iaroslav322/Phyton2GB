#4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
#должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
#числа используйте код:
#from random import randint
#num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

def input_data():
    a = -1
    while a < 0 or a > 1000:
        try: a = int(input("Введите a от 1 до 1000: "))
        except: print ("Введите число:")
    return a


b = randint(0,1000)
flag = 'проиграл'
step = 10
print(f'Число от 0 до 1000 загадано. Ходите\n')
while step !=0:
    a = int(input("Введите a от 1 до 1000: "))
    if a > b:
        print (f'Меньше')
        step -= 1
    elif a < b:
        print (f'Больше')
        step -= 1    
    elif a==b:
        flag = 'угадал'
        break
if step == 0:
    print(f"Ходы закончились ты {flag}")
else: print(f'Ты {flag}')
