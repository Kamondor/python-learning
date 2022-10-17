mahsulotlar = ["yog'", 'shakar', 'un', 'pishloq', 'sut', 'non', 'uzum', 'olma', 'mayiz', 'margarin']
yangi_savat = []

for n in range(5):
    yangi_savat.append(input(f"{n+1}-mahsulotni kiriting: "))
for taom in yangi_savat:
    if taom in mahsulotlar:
        print(f"{taom.title()} mahsulot do'konimizda bor")
    else:
        print(f"{taom.title()} mahsulot do'konimizda yo'q")
