input_number = input("Введите число: ")

try:
    number = float(input_number)
except ValueError:
    print("Введенное значение не является числом.")
else:
    if number % 3 == 0:
        print(f"{number} можно разделить на 3 без остатка.")
    else:
        print(f"{number} нельзя разделить на 3 без остатка.")