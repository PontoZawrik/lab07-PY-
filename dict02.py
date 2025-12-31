items = {
    "палатка": 5,
    "спальный мешок": 3,
    "удочка": 2,
    "термос": 2,
    "салфетки": 1,
    "жвачка": 1,
    "фонарик": 2,
    "карта": 1,
    "компас": 1,
    "аптечка": 2,
    "бутылка воды": 2,
    "куртка": 3,
    "нож": 1,
    "верёвка": 2,
    "газовая горелка": 3,
    "кастрюля": 2,
    "книга": 1,
}

sorted_items = sorted(items.items(), key = lambda item: -item[1])

n = int(input("Введите вес: "))

total_weight = 0
for name, weight in sorted_items:
    total_weight += weight

    if total_weight <= n:
        print(name)
    else:
        break