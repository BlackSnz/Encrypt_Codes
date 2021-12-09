# TODO ВЫПОЛНИТЬ МЕХАНИЗМ ПРОВОРОТОВ РОТОРОВ В ЗАВИСИМОСТИ ОТ ИХ ПОЛОЖЕНИЯ
# КОДИРОВКА ПОПАРНЫХ СОЕДИНЕНИЙ

# Словари цепочек модификаций символов для различных роторов
rotor_dict = {
    1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
    2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
    3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N')
    #4: 
    #5:
    #6:
    #7:
    #8:
    #9:
    # BETA ROTOR
    #10:
    # GAMMA ROTOR
    #11:
}

# Словарь проворота роторов
rotor_shift_dic = {
    1: (71),
    2: (5),
    3: (22),
    4: (10),
    5: (0),
    6: (0, 13),
    7: (0, 13),
    8: (0, 13)
}

# Словари цепочек модификаци символов для различных отражателей
reflector_dict = {
    # reflector B
    1: ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW')
    # reflector C
    #2:
    # reflector B Dunn
    #3:
    # reflector C Dunn
    #4:
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def start_enigma():
    print('Добро пожаловать в программу работы с энигмой')
    start_values()

# Реализация прохождение сигнала через ротор (смена символа в зависимости от номера ротора)
# Передаются: символ поступивший на ротор(symbol), номер ротора из словаря(n)
# Переменная reverse - предназначена для обратного хода сигнала (по умолчанию сигнал прямой reverse = False)
# Возвращает модифицированный символ исходя из цепочки модификации ротора
def rotor(symbol, n, reverse=False):
    symbol_number = 0
    for text in rotor_dict[n]:      # Поиск символа в словаре ротора
        if symbol in text:
            symbol_number = text.find(symbol)
            if reverse:             # Обратное направление
                if symbol_number > 0:
                    next_symbol = text[symbol_number - 1]
                else: 
                    next_symbol = text[-1]
            else:                   # Прямое направление
                if symbol_number < len(text) - 1:
                    next_symbol = text[symbol_number + 1]
                else: 
                    next_symbol = text[0]
    return next_symbol

# Реализация отражателя
def reflector(symbol, n):
    symbol_number = 0
    for text in reflector_dict[n]:      # Поиск символа в словаре отражателя
        if symbol in text:
            symbol_number = text.find(symbol)
            if symbol_number == 0:
                next_symbol = text[1]
            else:
                next_symbol = text[0]
    print(f'Проход сигнала через отражатель:\n{next_symbol}')
    return next_symbol

# Инициализация стартовых значений для функции !start_enigma!
def start_values():
    rotor_combination = input("Введите какие роторы будете использовать (Например: 231 - второй, третий, первый): ") # Справа налево
    print("Смещения роторов:")
    rotor_shift = []
    for char in rotor_combination:
        rotor_shift.append(int(input(f"Введите смещение {char}-го ротора: ")))
    reflector_name = int(input("Введите номер рефлектора: "))
    symbol = input(f'Введите букву, которую необходимо зашифровать: ')

    #Отрисовка машины с роторами и смещениями
    '''
    print('|========================================================|')
    print('|==              E   N   I   G   M   A                 ==|')
    print('|========================================================|')
    print(f'|==    ROTOR {rotor_combination[2]}         ROTOR {rotor_combination[1]}         ROTOR {rotor_combination[0]}         ==|')
    print('|==       ||             ||              ||            ==|')
    print('|==       ||             ||              ||            ==|')
    print('|==       ||             ||              ||            ==|')
    print(f'|==    {rotor_shift[2]}  ||          {rotor_shift[1]}  ||           {rotor_shift[0]}  ||            ==|')
    print('|==       ||             ||              ||            ==|')
    print('|==       ||             ||              ||            ==|')
    print('|==       ||             ||              ||            ==|')
    print('|========================================================|')
    print('|========================================================|')
    
    '''
    return encrypting_enigma(rotor_combination, rotor_shift, reflector_name, symbol)

# Функция смещение символа с параметром смещения.
def symbol_shifted(symbol, shift_amount):
    next_symbol = symbol
    try:
        next_symbol = alphabet[alphabet.find(next_symbol) + shift_amount]
    except IndexError:
        next_symbol = alphabet[(alphabet.find(next_symbol) + shift_amount) % 26]
    print(f'Смещение буквы {symbol} на {shift_amount}:\n{next_symbol}')
    return next_symbol 


# Запуск энигмы
def encrypting_enigma(rotor_combination, rotor_shift, reflector_name, symbol):
    if len(rotor_combination) == 1:     # Если ротор один
        rotor_shift[0] += 1
        next_symbol = symbol_shifted(symbol, rotor_shift[0])
        next_symbol = rotor(next_symbol, int(rotor_combination))
        print(f'Смещение в прямом направлении на роторе:\n{next_symbol}')
        next_symbol = symbol_shifted(next_symbol, -rotor_shift[0])
        next_symbol = reflector(next_symbol, reflector_name)
        next_symbol = symbol_shifted(next_symbol, rotor_shift[0])
        next_symbol = rotor(next_symbol, int(rotor_combination), reverse=True)
        print(f'Смещение в обратном направлении на роторе:\n{next_symbol}')
        next_symbol = symbol_shifted(next_symbol, -rotor_shift[0])
     
    else:       # Если роторов больше одного
        # Проверка проворотов роторов
        rotor_shift[0] += 1
         
        for rotor_number in range(0, len(rotor_combination) - 1):
            if rotor_shift[rotor_number] == rotor_shift_dic[int(rotor_combination[rotor_number])]:
                rotor_shift[rotor_number + 1] += 1
        next_symbol = symbol_shifted(symbol, rotor_shift[0])

        # Прямой ход сигнала
        for rotor_count in range(0, len(rotor_combination)):
            if rotor_count != len(rotor_combination) - 1:     # Проверка прихода сигнала к левому ротора
                next_symbol = rotor(next_symbol, int(rotor_combination[rotor_count]))
                print(f'Смещение в прямом направлении на роторе {int(rotor_combination[rotor_count])}:\n{next_symbol}')
                next_symbol = symbol_shifted(next_symbol, rotor_shift[rotor_count + 1] - rotor_shift[rotor_count])
            else: 
                next_symbol = rotor(next_symbol, int(rotor_combination[-1]))
                print(f'Смещение в прямом направлении левого ротора:\n{next_symbol}')
                next_symbol = symbol_shifted(next_symbol, 0 - rotor_shift[rotor_count])
        # Отражение в рефлекторе
        next_symbol = reflector(next_symbol, reflector_name)
        reversed_rotor_combination = ''.join(reversed(rotor_combination))
        reversed_rotor_shift = list(reversed(rotor_shift))
        temp = []
        for i in reversed_rotor_shift:
            i *= -1
            temp.append(i)
        reversed_rotor_shift = temp

        next_symbol = symbol_shifted(next_symbol, -(-rotor_shift[len(rotor_combination) - 1]))
        
        # Обратный ход сигнала
        for rotor_count in range(len(rotor_combination) - 1, -1, -1):
            if rotor_count > 0:     # Проверка прихода сигнала к левому ротора
                next_symbol = rotor(next_symbol, int(rotor_combination[rotor_count]), reverse=True)
                print(f'Смещение в обратном направлении на роторе {int(rotor_combination[rotor_count])}:\n{next_symbol}')
                next_symbol = symbol_shifted(next_symbol, rotor_shift[rotor_count - 1] - rotor_shift[rotor_count])
            else: 
                next_symbol = rotor(next_symbol, int(rotor_combination[0]), reverse=True)
                print(f'Смещение в обратном направлении правого ротора:\n{next_symbol}')
                next_symbol = symbol_shifted(next_symbol, 0 - rotor_shift[rotor_count])
        return next_symbol
    

start_enigma()

    
    
