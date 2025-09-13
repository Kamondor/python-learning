first_number = int(input("Birinchi sonni kiritng:\n"))
second_number = int(input("Ikkinchi sonni kiritng:\n"))
#foydalanuvchidan son olish


kopaytiruv = first_number*second_number
boluv = first_number/second_number
qoshuv = first_number + second_number
ayiruv = first_number - second_number
#arifmetik amallarni bajarib, o'zgaruvchiga yuklash
if first_number/second_number ==int(first_number/second_number):
    boluv = int(boluv)
else:
        boluv = boluv

print(f"{first_number} ga {second_number} ni qo'shsa {qoshuv} bo'ladi")
print(f"{first_number} ni {second_number} dan ayirsa {ayiruv} bo'ladi")
print(f"{first_number} ni {second_number} ga ko'paytirsa {kopaytiruv} bo'ladi")
print(f"{first_number} ni {second_number} ga bo'lsa {boluv} bo'ladi")
