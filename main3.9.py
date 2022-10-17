cars = ['bmw', 'audi', 'tesla', 'mercedes', 'volvo', 'chevrolet', 'UzAuto']
cars.sort() #bosh harf bo'yicha tartiblash

new_cars =  sorted(cars) # asl ro'yxatga ta'sir qilmasdan tartiblaydi

teskari_cars = sorted(cars, reverse = True) # yuqoridagidan teskari tartiblash

len_cars = len(cars) # Ro'yxat uzunligi - elementlar soni

fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']

fruits.reverse()

sonlar = list(range(0,201,2))  #range 0 dan 200 gacha 2 qadamda sonlarni generat-
# siyalaydi

narxlar = [12000, 22500,23456, 9800, 5600, 9934, 32874]

arzon = min(narxlar) # Ro'yxatdagi eng kichik sonni aniqlaydi
qimmat = max(narxlar) # Ro'yxatdagi eng katta sonni aniqlaydi
jami = sum(narxlar) # Ro'yxat elementlari yig'indisi aniqlaydi

sonlar2 = sonlar[0:20] # Indeksi 0 dan 19 gacha bo'lgan elementlarni kesib  oladi
sonlar3 = sonlar[2:] # Indeksi 2 ga teng sondan oxirigacha ro'yxatni kesib oladi
sonlar4 = sonlar[:4] # Indeksi 4 ga teng songacha ro'yxatni kesib oladi
clone_sonlar = sonlar[:] # Ro'yxatni butunlay ko'chirib oladi

tuple_royxat = ('car', 'mcqueen', 'dino', 'snake', 'lizard', 'dragon') # O'zgartirib bo'lmaydigan
# ro'yxat
list_function = list(tuple_royxat) # List() funksiyasi o'zgaradigan ro'yxatga o'zgartiradi

print('Kesilgan elementlar:\n', sonlar2)

print('Eng arzon narx', arzon,\
      'Eng qimmat narx ', qimmat,\
      ".Jami: ", jami)

print(f"1 dan 200 gacha juft sonlar:\n {sonlar}")

print(f"Elementlar soni {len_cars} ga teng")
print(cars)
print(fruits)
