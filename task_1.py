# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import pi

accuracy = float(input('Ввеидите необходимую точность числа ПИ: '))
count=0
while accuracy%1 > 0:
    accuracy*=10
    count+=1
if 10**-1>=10**-count>=10**-10:
    print(f'π = ',round(pi,count))
else: print('Введите корректную точность числа')
