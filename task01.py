eng = {
    1: "AEIOULNSTR",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
rus = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}

word = input("Введите слово: ")
if word.isalpha():
    word = word.upper()

    tDict = rus
    for score, letters in eng.items():
        if word[0] in letters:
            tDict = eng
            break

    total = 0
    for ch in word:
        for score, letters in tDict.items():
            if ch in letters:
                total += score
                break

    print(total)
else:
    print("Неверный ввод.")