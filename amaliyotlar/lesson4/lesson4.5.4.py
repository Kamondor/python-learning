k_mahsulotlar = []
bor_mahsulotlar = []
mavjud_emas = []
d_mahsulotlari = ["yog'", 'shakar', 'un', 'pishloq', 'sut', 'non', 'uzum', 'olma', 'mayiz', 'margarin']
for n in range(5):
    k_mahsulotlar.append(input(f"Biror mahsulotni kiriting: "))
    for mahsulot in k_mahsulotlar:
        if mahsulot in d_mahsulotlari:
            bor_mahsulotlar.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)
if len(mavjud_emas) == 0:
    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
else:
    for n in mavjud_emas:
        print(f"Quyidagi mahsulotlar do\'konimizda mavjud emas:{n}")
            

    
