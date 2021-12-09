import re

def jarriquez_encryption(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse = False):
    
    # Очистка текста
    clean_text = text.rstrip().upper()
    clean_text = re.sub(r'[^\w\s]','', clean_text)
    clean_text = clean_text.replace(' ', '')

    # Нахождение ключа каждой буквы введенного текста
    clean_text = list(clean_text)
    alphabet = list(alphabet)
    text_number_list = []
    for char in clean_text:
        text_number_list.append(alphabet.index(char))
        
    key_list = []
    j = 0
    result = []
    key = list(str(key))
    # Шифрование и дешифрование текста
    for i in range(0, len(clean_text)):
        if j >= len(key):
            j = 0
        key_list.append(key[j])
        j += 1
        if reverse == False:
            if int(text_number_list[i]) + int(key_list[i]) >= len(alphabet):
                result.append(alphabet[int(text_number_list[i]) + int(key_list[i]) - len(alphabet)])
            else: result.append(alphabet[int(text_number_list[i]) + int(key_list[i])])
        else:
            if int(text_number_list[i]) - int(key_list[i]) < 0:
                result.append(alphabet[int(text_number_list[i]) - int(key_list[i]) + len(alphabet)])
            else: result.append(alphabet[int(text_number_list[i]) - int(key_list[i])])
    print(f"Исходный текст: {text}\nКлюч шифрования: {''.join(key)}\nОбщий вид шифрования:\n{''.join(clean_text)}\n{''.join(key_list)}\nЗашифрованный текст: {''.join(result)}")
    return ''.join(result)
       

jarriquez_encryption('CFRXUGSJTLXNHW', 356, reverse= True)
    