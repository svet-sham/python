name = input("Привет, меня зовут Светлана. А как твое имя?")
print("Привет,", name)
print("Это моя первая программа на языке Python.")
programm_count = input("А сколько программ на языке Python ты написал?")
print("Поздравляю! Тобой написано", programm_count, "программ на языке Python")
number1 = 7
number2 = int(input("Введи любое целое число"))
sum = number1 + number2
print("Сумма твоего числа и моего числа составляет", sum)
option = int(input("Какое число я загадала?"))
if option == number1:
    print("Верно!")
else:
    print("Неверно, я загадала число", number1)
