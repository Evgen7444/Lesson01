a = int(input("Введите результат пробежки первого дня в км "))
b = int(input("Введите желаемый результат пробежек в км "))
result_days = 1
result_km = a
while result_km < b:
    a = a * 1.1
    result_days += 1
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)