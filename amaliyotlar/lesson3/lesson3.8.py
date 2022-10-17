davlatlar = ['Vatikan', "O'zbekiston", 'Rossiya', 'Ukraina', 'AQSh', 'Buyuk Britaniya']
sonlar = list(range(120,1200,2))
jami = sum(sonlar)
eng_katta = max(sonlar)
eng_kichik = min(sonlar)

ayirma = eng_katta - eng_kichik

#davlatlar.reverse()

davlatlar.sort(reverse = True)


davlatlar.sort()
print(davlatlar)

print(jami)
print(ayirma)
