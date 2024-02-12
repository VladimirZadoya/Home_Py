def calculate_expression(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    result = n + nn + nnn
    return result
number = int(input("Введите целое число: "))
print("Результат выражения n + nn + nnn равен:", calculate_expression(number))
