time = int(input("Введите время в секундах >>> "))
h = int(time // 3600)
m = int(time - h * 3600) // 60
s = time - (h * 3600 + m * 60)
print(f"Время в формате чч:мм:сс {h} : {m} : {s}")
