mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':20000,
    'anjir':25000,
    'shaftoli':30000
    }
# Lug'at

bozorlik = ['anor','uzum', 'non', 'baliq'] #ro'yxat
for  m in mahsulotlar:
    if m in bozorlik:
        print(f"{m.title()} {mahsulotlar[m]} so'm")
    else:
        print(f"Kechirasiz bizda {m.title()} yo'q")
        
