seconds = int(input("Введите количество секунд "))
hours = seconds // 3600
seconds = seconds - (hours * 3600)
minutes = seconds // 60
seconds = seconds - (minutes * 60)
print(f"Введеное вами время в формате ЧЧ:ММ:СС составляет {hours}:{minutes}:{seconds}")
