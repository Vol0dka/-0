#Импорт необходимых библиотек
import math
#Ввод высоты
h = float(input('Введите высоту: '))
#Рассчет скорости
v=math.sqrt(2*9.8*h)
#Вывод итога
print('Скорость при ударе:', v)