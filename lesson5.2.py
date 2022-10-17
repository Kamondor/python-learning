talaba = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'yadro',
    'kurs':4
    }
# lug'at 
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'nokia 3310 ',
    'orif':'mi 10 pro'
    }
#lug'at

mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':30000
    }
# Izoh: Narxlar shunchaki yozildi,Asliga noto'g'ri

for kalit, qiymat in talaba.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}")
# for orqali talaba lug'atimizni chiroyli chiqaramiz


for k, q, in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
print(talaba.items()) # items metodi orqali talaba lug'atimizni chiqaramiz

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys(): # keys() faqat lug'atning key larini chiqaruvchi funksiya
    print(mahsulot.title())


