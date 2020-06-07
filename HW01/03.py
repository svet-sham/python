number = int(input("Введите целое число от 0 до 9"))
sum_ = number + (number * 11) + (number * 111)
number2 = number * 11
number3 = number * 111
print(f"Вы ввели число {number}. Сумма чисел составляет {number} + {number * 11} + {number * 111} = {sum_}")
