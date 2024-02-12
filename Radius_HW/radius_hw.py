import math

def obchyslyty_ploshchu_kola():
    try:

        radius = float(input("Введіть радіус кола: "))


        area = math.pi * radius**2


        print(f"Площа кола з радіусом {radius} одиниць: {area:.2f}")
    except ValueError:
        print("Будь ласка, введіть числове значення для радіусу.")


obchyslyty_ploshchu_kola()