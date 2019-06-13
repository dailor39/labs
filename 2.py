def fun1(text):
    lst = text.split(' ')
    lst2 = []
    for elem in lst:
        if elem[:2] == 'Ли':
            lst2.append(elem)
    return ' '.join(lst2)

def fun2(text):
    lst = text.split('_')
    print('\tФИО\t\tВозраст\t\tКатегория')
    for elem in lst[1:]:
        a= elem.split(';')
        print(a[0] + ' ' +a[1]+' '+a[2]+'\t'+a[3]+'\t\t'+a[4])
def fun3(text):
    lst = text.split('_')
    for elem in lst[1:]:
        a = elem.split(';')
        if a[1] == '21 год':
            print(' '.join(a))
def fun4():
    n = int(input('Введите количество чисел '))
    lst = []
    for i in range(n):
        lst.append(int(input('Введите число ')))
    i = 1
    while i < len(lst):
        lst.pop(i)
        i+=1
    lst.append(int(input('Введите число ')))
    lst.append(int(input('Введите число ')))
    for elem in lst:
        print(str(elem))
