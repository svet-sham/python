number = int(input("Введите целое положительное число"))
max_figure = number % 10
figures: int = number // 10
while True:
    if figures < 1:
        break

    if figures <= 9:
        figure = figures
    else:
        figure = figures % 10

    if figure > max_figure:
        max_figure = figure
    figures = figures//10


print(f"Максимальная цифра из введенного вами числа составляет {max_figure}")
