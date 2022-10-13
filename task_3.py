# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
array = [1, 3, 5, 8, 9, 8, 3, 1, 5, 6]
new_array = []
for i in array:
    if i not in new_array:
        new_array.append(i)
print(array)
print(new_array)
