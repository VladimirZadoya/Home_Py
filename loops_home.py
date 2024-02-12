count = 1
while count <= 10:
    print(count)
    count += 1
user_input = input("Введіть число: ")
n = int(user_input)

sum_numbers = 0
for i in range(1, n + 1):
    sum_numbers += i

print(f"Сума чисел від 1 до {n}: {sum_numbers}")