profit = float(input("Введите выручку фирмы "))
cost = float(input("Введите издержки фипмы "))
if profit > cost:
    print(f"Фирма работает с прибылью. Рентабельность составляет {profit / cost * 100}%")
    people = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль на одного сотрудника составляет {profit / people}")
elif profit == cost:
    print("Фирма балансирует на нуле. Радоваться нечему!")
else:
    print("Фирма работает в убыток. Пора что-то делать!")
