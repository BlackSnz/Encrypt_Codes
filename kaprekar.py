from functools import reduce
import sys

print("Эта программа выводит иттерационный процесс функции Капрекара.\n")
print("Введите 3-х, 4-х или 6-ти значное число, в котором\nне все цифры в числе одинаковые\nчисло не равно 100, 1000 или 100 000:")
n = int(input())

#def kaprekar_check(n):
   # if n == 100 & n == 1000 & n == 100000:
    #    print("Число не удовлетворяет условию: число не равно 100, 1000 или 100 000") 
    #elif 
#Преобразует полученное число в список его цифр
def numerics(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n //= 10
    return result

# Проводит 1 шаг к постоянной Капрекара
def kaprekar_step(result):
    sorted_number_list = []
    for i in result:
        sorted_number_list.append(i)
    sorted_number_list.sort()

    reversed_sorted_number_list = []
    for i in result:
        reversed_sorted_number_list.append(i)
    reversed_sorted_number_list.sort()
    reversed_sorted_number_list.reverse()


    sorted_number = reduce(lambda x,y: 10*x+y, (sorted_number_list))
    reversed_sorted_number = reduce(lambda x,y: 10*x+y, (reversed_sorted_number_list))

    n = reversed_sorted_number - sorted_number
    return n

def kaprekar_loop(n):
    step = 0
    while n != 6174:
        n = kaprekar_step(numerics(n))
        step +=1
        print(f"{step} шаг иттерации: {n}")

kaprekar_loop(n)
