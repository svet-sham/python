revenue = float(input("Введите выручку вашей фирмы в рублях"))
costs = float(input("Введите издержки вашей фирмы в рублях"))
fin_results = revenue - costs
if fin_results < 0:
    print("Ваша фирма работает в убыток. Убыток составляет {:.2f} рублей".format(0 - fin_results))
else:
    profit_margin = fin_results / revenue * 100
    print("Ваша фирма получила прибыль в размере {:.2f} рублей. Рентабельность выручки составила {:.2f}%".format(
        fin_results, profit_margin))
    workers = int(input("Введите количество сотрудников вашей фирмы"))
    print("Прибыль вашей фирмы в расчете на одного сотрудника составляет {:.2f} рублей".format(fin_results / workers))
