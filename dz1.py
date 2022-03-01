1
number = input('Введите число: ')

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)

print(f"Сумма цифр числа {number}: {sum}")
print(f"Произведение цифр: {number}: {prod}")




year = int(input('Введите год: '))

if year % 400 == 0:
    print(f"Год {year} високосный")
elif year % 100 == 0 and year % 400 != 0:
    print(f"Год {year} невисокосный")
elif year % 4 == 0:
    print(f"Год {year} високосный")
else:
    print(f"Год {year} невисокосный")






n3, n2, n3 = [x for x in input('Введите три числа, через пробел: ').split()]


if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')
    
    
    2
