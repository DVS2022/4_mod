def massiv(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 
 
alist = input('Введите массив чисел через пробел: ').split()
alist = [int(x) for x in alist]
massiv(alist)
print('Отсортированный массив: ', end='')
print(alist)