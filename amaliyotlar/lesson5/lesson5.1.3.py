python = {
    'if':'Agar degan ma\'noni beradi.Shart tekshiruvchisi',
    'float':'Sonning o\'nlik turi.Masalan, 10.5',
    'integer':'Butun son',
    'string':'Matn,',
    'else':'If ga yozilgan shart qanoatlantirilmasa, else ga yozilganlar ishga tushadi',
    'list':'O\'zgartirish mumkin bo\'lgan ro\'yxat',
    'tuple':'() bilan belgilangan bo\'lib, o\'zgarmaydi',
    }


kalit = input("Kalit so'z kiriting:").lower()
kalitlar = []
kalitlar.append(python.get(kalit, 'Bunday so\'z topilmadi'))
print(kalitlar)
