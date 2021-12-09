"""
Autor: Evgeny Gorupay
Ecrypt & Decrypt Cesar code programm

"""

import re
import sys

print("--------------------------------------------------------------------")
print("     //// Данная программа работает с шифром Цезаря. ////\n//// Вы можете зашифровать текст(1), либо подобрать ключ(2) ////")
print("--------------------------------------------------------------------")

# Отвечает за старт программы
def startprogram():
    print("Выберите режим работы программы:\n1. Зашифровать текст\n2. Подобрать ключ")
    user_choise = int(input("Ваш выбор: "))
    print("--------------------------------------------------------------------")
    if user_choise == 1:
        text_ecrypt()
    elif user_choise == 2:
        text_decrypt()
    else:
        print("Необходимо ввести '1' или '2'")
        print("Попробуйте ещё раз...")
        startprogram()
    final()

# Отвечает за финал программы1
def final():    
    final_choise = input("Хотите продолжить работу с программой? (y/n): ")
    if final_choise == 'y':
        startprogram()
        print("--------------------------------------------------------------------")
    elif final_choise != 'n':
        print("Неправильный ввод.")
        print("--------------------------------------------------------------------")
        final()
        
    else:
        sys.exit()

# Отвечает за выбор режима шифрования текста
def text_ecrypt():
    print("Выберите режим работы с алфавитом:\n1. Собственный алфавит\n2. Английский алфавит")
    user_choise = int(input("Ваш выбор: "))
    print("--------------------------------------------------------------------")
    if user_choise == 1:
        print("Введите алфавит для шифрования:")
        alphabet = input('Ваш алфавит: ')
        print("--------------------------------------------------------------------")
        print("Введите текст, который необходимо зашифровать.")
        text = input("Ваш текст: ")
        print("--------------------------------------------------------------------")
        print("Введите ключ смещения: ")
        key = int(input("Ваш ключ: "))
        print("--------------------------------------------------------------------")
        print(f"Исходный текст: {text}\nЗашифрованный текст: {caesar(text, key, alphabet)}")
        print("--------------------------------------------------------------------")
        
    elif user_choise == 2:
        print("Введите текст, который необходимо зашифровать.")
        text = input("Ваш текст: ")
        print("--------------------------------------------------------------------")
        print("Введите ключ смещения: ")
        key = int(input("Ваш ключ: "))
        print("--------------------------------------------------------------------")
        print(f"Исходный текст: {text}\nЗашифрованный текст: {caesar(text, key)}")
        print("--------------------------------------------------------------------")
    else:
        print("Необходимо ввести '1' или '2'")
        print("Попробуйте ещё раз...")
        text_ecrypt()

# Отвечает за выбор режима расшифровки текста
def text_decrypt():
    print("Выберите режим работы с алфавитом:\n1. Собственный алфавит\n2. Английский алфавит")
    user_choise = int(input("Ваш выбор: "))
    print("--------------------------------------------------------------------")
    if user_choise == 1:
        print('Введите алфавит для расшифровки:')
        alphabet = input('Ваш алфавит: ')
        print("--------------------------------------------------------------------")
        print("Введите текст, который необходимо расшифровать: ")
        text = input("Ваш текст:")
        print("--------------------------------------------------------------------")
        bruteforce(text, alphabet)
    elif user_choise == 2:
        print("Введите текст, который необходимо расшифровать: ")
        text = input("Ваш текст:")
        print("--------------------------------------------------------------------")
        bruteforce(text)
    else:
        print("Необходимо ввести '1' или '2'")
        print("Попробуйте ещё раз...")
        print("--------------------------------------------------------------------")
        text_decrypt()

# Отвечает за шифрование текста
def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    alphabet_list = list(alphabet.lower())
    # Очистка текста
    clean_text = text.rstrip().lower()
    clean_text = re.sub(r'[^\w\s]','', clean_text)
    clean_text = clean_text.replace(' ', '')

    result = []
    if (key//len(alphabet_list)) != 0:
        key = key - len(alphabet_list)*(key//len(alphabet_list))
    for i in clean_text:
        if (key + alphabet_list.index(i) + 1) > len(alphabet_list):
            result.append(alphabet_list[alphabet_list.index(i) + key - len(alphabet_list)])
        else:
            result.append(alphabet_list[alphabet_list.index(i) + key])
    return ''.join(result)

# Отвечает за расшифровку текста
def bruteforce(text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for i in range(len(alphabet) - 1, 0 , -1):
        print(f"Ключ: {i} || Результат дешифровки: {caesar(text, i, alphabet)}")
    print("--------------------------------------------------------------------")

startprogram()