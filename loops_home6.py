user_input = input("Введіть число: ")
n = int(user_input)
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факторіал числа {n}: {factorial}")
decimal_number = int(input("Введіть число в десятковій системі: "))
binary_number = bin(decimal_number)

print(f"Двійкове представлення числа {decimal_number}: {binary_number}")