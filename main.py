import cesar as ces

try:
    user_key = int(input('Введите значение ключа: если '
         'нужно сдвинуть вправо - положительное число, влево - отрицательное\n'))
except ValueError:
    print ('Некорректный ввод! Введите число!')
user_file_key = input('Введите название для файла, в котором будет храниться ключ\n')
with open(user_file_key, 'w', encoding="utf-8") as f1:
    f1.write(str(user_key))
object_shifvr = input('Введите путь до файла, который нужно зашифровать\n')
object_shifvr_2 = input('Введите название файла, в котором будет зашифрованный текст\n')
with open(object_shifvr_2, 'w', encoding="utf-8") as f3:
    with open(object_shifvr, 'r', encoding="utf-8") as f2:
        for line in f2:
            for symbol in line:
                if symbol.isalpha() == True:
                    pt = ces.Cesar(ord(symbol), user_key)
                    f3.write(chr(ces.Cesar.STR(pt)))
                else:
                    f3.write(symbol)
