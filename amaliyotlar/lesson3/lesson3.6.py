cars = [] #bo'sh ro'yxat
cars.append('Lacetti') #ro'yxatning oxiriga qo'shish
cars.append('Cobalt')  #ro'yxatning oxiriga qo'shish
cars.append('Nexia 3') #elementni indeksi bo'yicha o'chiradi
del cars[1]  # 2- elementni o'chirib tashlaydi
cars.insert(0, 'Malibu')  # 1-element bo'lib qo'shiladi
cars.remove("Malibu") # elmentni nomi bo'yicha o'chiradi

nexia=cars.pop(1)   
print(cars)
print(nexia)
