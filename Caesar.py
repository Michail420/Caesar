a = int(input('Введите значение смешения: '))
txt = (input('Введите текст: '))
alfa = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

 
def Caesar(txt, shift=a):
    abc = ""
    for x in txt:
        if x in alfa:
            ind = alfa.index(x)
            abc += alfa[ind+shift] 
        else:
            abc += x
    return abc
 
def AntiCaesar(txt, shift=a):
    abc = ""
    for x in txt:
        if x in alfa:
            ind = alfa.index(x)
            abc += alfa[ind-shift]
        else:
            abc += x
    return abc
print ('\n')
print('Результат шифровки :',Caesar(txt))
print('Результат расшфровки :',AntiCaesar(txt))
