n = int(input("Введите количество строк: "))
purchases = {}

for _ in range(n):
    line = input().split()
    buyer, product, count = line[0], line[1], int(line[2])

    if buyer not in purchases:
        purchases[buyer] = []
    purchases[buyer].append((product, count))

print("Результат: ")
for buyer in sorted(purchases.keys()):
    print(f"{buyer}:")
    for product, count in purchases[buyer]:
        print(f"{product} {count}")