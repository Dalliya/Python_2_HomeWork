#Сгенерировать массив (list()). из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.

num_limit = 101
list = []
for i in range(num_limit):
    if i % 2 == 0:
        list.append(i)
print(list)



