number_list = []

def multiplication_check_list(start=10, stop=99):
    true_results = 0
    false_results = 0
    for i in range (start, stop + 1):
        for j in range (start, stop + 1):
            if multiplication_check(i, j):
                true_results += 1
            else: 
                false_results +=1
    print(f"Правильных результатов: {true_results}")
    print(f"Неправильных результатов: {false_results}")



def simple_multiplication(x, y):
    result = (100-((100-x)+(100-y)))*100 + (100-x)*(100-y)
    print(f"{x} * {y} = {result}")
    return result

def multiplication_check(x, y):
    return x*y == simple_multiplication(x, y)

def wisdom_multiplication(x,y, length_check = True):
    first_number = str(100-((100-x)+(100-y)))
    second_number = str((100-x)*(100-y))
    if length_check & len(second_number) < 2:
        second_number = "0" + str(second_number)
    result = int(first_number + second_number)
    print(result)
    return result

def wisdom_multiplication_check(x, y):
    return x*y == wisdom_multiplication(x, y)

def wisdom_check_list(start=10, stop=99, length_check=True):
    true_results = 0
    false_results = 0
    for i in range (start, stop + 1):
        for j in range (start, stop + 1):
            if wisdom_multiplication_check(i, j):
                true_results += 1
            else: 
                false_results +=1
    print(f"Правильных результатов: {true_results}")
    print(f"Неправильных результатов: {false_results}")
    
wisdom_check_list()
