son = int(input("Istalgan butun sonni kiriting: "))
boluvchilar = [2, 3, 5, 7, 11, 13, 17, 23, 31, 37, 43, 47]
for boluv in boluvchilar:
    if son%boluv == 0:
        print(f"{son} soni {boluv} ga bo'linadi")
    else:
        print(f"Bu {son} soni {boluv} tub songa bo'linmaydi")
