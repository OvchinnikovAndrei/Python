# Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите трехзначное число: "))
 
d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
 
print("Сумма цифр числа:", n + d1 + d2)