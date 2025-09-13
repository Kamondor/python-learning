viloyat = str(input("Qaysi viloyatdansiz?\n"))
tuman = str(input("Tumaningizni kiriting:\n"))
mahalla = str(input('Mahallangizni kiriting:\n'))
kocha = (input("Ko'changizni kiriting:\n"))
#foydalanuvchi ma'lumotni olish

viloyat = viloyat.strip()
tuman = tuman.strip()
mahalla = mahalla.strip()
kocha = kocha.strip()

manzil = f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko'chasi"
#ma'lumotni o'zgaruvchiga yuklash

#natijani chiqarish
print(f"{viloyat.title()} viloyati, {tuman.title()} tumani, {mahalla.title()} mahallasi, {kocha.title()} ko'chasi" )
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())

