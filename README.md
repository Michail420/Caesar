# Шифр Цезаря
## Описание программы 
Шифр Цезаря заключается в замене каждого символа входной строки на символ, находящийся на несколько позиций левее или правее его в алфавите.Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.
## Manual
### Описание назначения.
Программа предназначена для шифровки и расшифровки текста по принципу Цезаря. Шифр Цезаря заключается в замене каждого символа входной строки на символ, находящийся на несколько позиций левее или правее его в алфавите. Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.

### Запуск программы.
При запуске программа просить ввести целое число, от которого будет зависеть количество сдвигов в алфавите. Если ввести символ или дробное число, программа будет повторять  запрос ввести целое число до тех пор, пока вы не введете его. После того, как вы ввели целое число, она попросить ввести текст. Если вводить текст заглавными буквами или на английском программа не сможет выполнить свою работу и выдаст исходный текст без изменений. Чтобы программа выполняла свою функцию, следует вводить текст на русском языке строчными буквами.

### Выполнение основных функций.
Если вы ввели все правильно, программа зашифрует и расшифрует введенный текст. При шифровке, программа меняет каждый символ текста на следующий, находящийся на заданное количество позиций правее его в алфавите. При расшифровке происходит схожий процесс, только смещение идет влево.

### Завершение программы.
После выполнения своей функции программа выдаст два варианта введенного ранее текста. Первый вариант будет зашифрованным текстом, а второй расшифрованным. Чтобы программа выполняла свою функцию, следует вводить текст на русском языке строчными буквами. Иначе программа выдаст исходный текст без изменений.
## Скриншоты
![Иллюстрация к проекту](https://github.com/Michail420/Caesar/blob/master/Caesar.PNG)
## Описание среды 
Программа написана на языке Python в среде Spyder. Следует открывать файл Caesar.py. В нем будет находиться программа ,для работы с которой нужно ввести целое число сдвигов и фразу для перевода. Программа выдаст сразу расшифрованный и зашифрованный вариант фразы, которую вы ввели.
