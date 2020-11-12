import logging

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'loger.log')

def sapros(ogranbas,watt,par_1,par_2): #фунция запроса и проверки значения ответа 
    go = True
    while go == True:
        ye = 0     
        bas = [1,0]
        if ogranbas == True: print('----------\n'+watt+':\n0 - '+par_1+'\n1 - '+par_2)
        else: print('----------\n'+watt)
        vosvrat = input(':')
        if  vosvrat.isdigit() == True:
            vosvrat = int(vosvrat)
            go = False
            logging.debug(u"число введено в правильном формате")
        else:
            go = True
            print('необходимо целое число')
            logging.debug(u"выбран неверный формат")
        if ogranbas != True: continue
        for i in bas:
            if vosvrat == i: ye +=1 
        if ye == 1: go = False 
        else:
            print('Введеное значение не совпадает с возможными')
            logging.debug(u"Введеное значение не совпадает с возможными")
            go = True
    return vosvrat 

#проверяет соответствие типов венных данных с требуемыми
logging.info(u"Программа начала работу")    
while True:
    try:
        a = int(input("Введите число: "))
        logging.info(u"пользователь ввел число смещений")
        break
    except ValueError:
        logging.debug(u"Введеное значение не совпадает с возможными")
        print ('\n')
        print("Вы ввели не целое число. Попробуйте снова: ")

txt = (input('Введите текст: '))
logging.info(u"введен текст")      
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
logging.info(u"выведен результат")
logging.info(u"Программа закончила работу") 
