n = int(input("Максимальное число: "))

possible = set(range(1, n + 1))

while True:
    line = input()
    if line.upper() == "HELP":
        break

    data = line.split()
    nums = set(map(int, data[:-1]))
    answer = data[-1].upper()

    if answer == "YES":
        possible = possible & nums
    elif answer == "NO":
        possible = possible - nums

print(*sorted(possible))