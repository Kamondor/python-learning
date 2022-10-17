korishgan_son = int(input('Bugun necha kishi bilan ko\'rishdingiz?\n'))
odamlar = []
for n in range(korishgan_son):
    odamlar.append(input(f"{n+1}-odam ismini kiriting: ").title())

print(odamlar)
print(len(odamlar))
