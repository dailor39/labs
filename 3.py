import os

def fun1():
    path = input('Введите путь ')
    lst = os.listdir(path)
    count = 0
    for elem in lst:
        if '.' in elem:
            count+=1
    print(count)
def fun2(mlst):
    if not len(mlst) == 0:
        for elem in mlst:
            print(' '.join(elem))
        return mlst
    f = open('products.txt','r')
    text = f.read()
    f.close()
    lst = list(map(lambda x:x.split(';'),text.split('\n')))[1:]
    lst.sort(key = lambda x:int(x[2]))
    for elem in lst:
        print(' '.join(elem))
    return lst

def fun3(mlst):
    a = list(map(lambda x:int(x),input('Введите id товаров в виде "1 5 12 13 " ').split(' ')))
    b = int(input('Введите насколько уменьшить количество '))
    for i in range(len(mlst)):
        if int(mlst[i][0]) in a:
            mlst[i][3]=str(int(mlst[i][3])-b)
    for elem in mlst:
        print(' '.join(elem))
    return mlst

def fun4(mlst):
     f = open('products.txt','w')
     f.write('№;Наименование_товара;Цена;Количество')
     for elem in mlst:
         f.write('\n')
         f.write(';'.join(elem))
     f.close()
         
    
def menu(mlst):
    print('')
    print('0 - Выход из программы')
    print('1 - Посчитать кол-во файлов в заданной директории')
    print('2 - Вывод информации о товарах и считывание для пунктов 3,4')
    print('3 - Увеличение цены товаров')
    print('4 - Сохранить')
    a = int(input('Ввод '))
    print('')
    if a == 0:
        return mlst
    if a == 1:
        fun1()
        if int(input('Выход из программы? 1 - да, 0 - нет. '))== 1:
               return mlst
        menu(mlst)
    if a == 2:
        mlst = fun2(mlst)
        if int(input('Выход из программы? 1 - да, 0 - нет. ')) == 1:
            return mlst
        menu(mlst)
    if a == 3:
        mlst = fun3(mlst)
        if int(input('Выход из программы? 1 - да, 0 - нет. '))== 1:
               return mlst
        menu(mlst)
    if a == 4:
        fun4(mlst)
        if int(input('Выход из программы? 1 - да, 0 - нет. '))== 1:
               return mlst
        menu(mlst)
    print('')
menu([])
