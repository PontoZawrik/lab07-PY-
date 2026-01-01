n = int(input("количество кубиков у Тани: "))
m = int(input("количество кубиков у Коли: "))

print("Номера цветов кубиков Тани:", end="\n")
tanya = {int(input()) for _ in range(n)}

print("Номера цветов кубиков Тани:", end="\n")
kolya = {int(input()) for _ in range(m)}

print("=========================")

common = sorted(kolya & tanya)
print(f"Количество совпадений: {len(common)}")
print(*common)

only_tanya = sorted(tanya - kolya)
print(f"Количество цветов, которые остались у Тани: {len(only_tanya)}")
print(*only_tanya)

only_kolya = sorted(kolya - tanya)
print(f"Количество цветов, которые остались у Коли: {len(only_kolya)}")
print(*only_kolya)