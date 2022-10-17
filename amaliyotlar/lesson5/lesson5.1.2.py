python = {
    'if':'Agar degan ma\'noni beradi.Shart tekshiruvchisi',
    'float':'Sonning o\'nlik turi.Masalan, 10.5',
    'integer':'Butun son',
    'string':'Matn,',
    'else':'If ga yozilgan shart qanoatlantirilmasa, else ga yozilganlar ishga tushadi',
    'list':'O\'zgartirish mumkin bo\'lgan ro\'yxat',
    'tuple':'() bilan belgilangan bo\'lib, o\'zgarmaydi',
    }
#search_word = input('Pythondagi atamani kiriting: ')
#key_error = python.get(search_word, 'Bunday kalit mavjud emas')

kalit = input("Kalit so'z kiriting:").lower()
print(python.get(kalit, "Bunday so'z mavjud emas"))

#print(python[search_word])

