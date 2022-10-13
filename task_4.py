# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
k = int(input('Введите степень: '))

kf = list()
for i  in range(1, k+2):
    kf.append(randint(1,100))
polynomial = list()
for i in range(len(kf)):
    if k==0:
        polynomial.append(f'{kf[i]}')
    elif k==1:
        polynomial.append(f'{kf[i]}x+')
    else:
        polynomial.append(f'{kf[i]}x^{k}+')
    k-=1    
polynomial.append('=0')
fout = open('digit.txt', 'w')
fout.write(''.join(polynomial))
fout.close() 