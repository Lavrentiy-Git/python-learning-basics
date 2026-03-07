import time, sys

direction_right = True # направление движения. True - расширение, False - сужение
spaces = 10 # начальное значение количества пробелов
stars = 1 # начальное значение количества звезд

print("Анимация ёлочки / ромба. Нажмите Ctrl+C для выхода.\n")

while True:
    try:
        print(spaces * " " + "*" * stars) # вывод текущей строки
        time.sleep(0.1) # Задержка для плавности
        if direction_right:
            # Расширение за счет изменения значений переменных stars и spaces
            stars += 2
            spaces -= 1
            # Если дошли до края - изменяем направление движения  
            if spaces == -1:
                direction_right = False
        if not(direction_right):
            # Сужение звезд
            stars -= 2
            spaces += 1
            # Если дошли до края - назначаем значения переменных заново
            if spaces > 10:
                stars = 3
                spaces = 9
                direction_right = True
    except KeyboardInterrupt:
        sys.exit()
