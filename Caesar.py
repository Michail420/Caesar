#проверяет соответствие типов венных данных с требуемыми
while True:
    try:
        a = int(input("Введите число: "))
        break
    except ValueError:
        print ('\n')
        print("Вы ввели не целое число. Попробуйте снова: ")

txt = (input('Введите текст: '))      
alfa = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

#заменяет каждый символ txt на символ, находящийся на shift позиций правее в alfa
def Caesar(txt, shift=a):
    abc = ""
    for x in txt:
        if x in alfa:
            ind = alfa.index(x)
            abc += alfa[ind+shift]     
    return abc
#заменяет каждый символ txt на символ, находящийся на shift позиций левее в alfa  
def AntiCaesar(txt, shift=a):
    abc = ""
    for x in txt:
        if x in alfa:
            ind = alfa.index(x)
            abc += alfa[ind-shift]
    return abc
print ('\n')
print('Результат шифровки :',Caesar(txt))
print('Результат расшфровки :',AntiCaesar(txt))
