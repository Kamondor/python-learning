yosh = int(input('Yoshingiz nechida?\n'))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh <65:
    price = 10000
elif yosh >=65:
    price = 8000
print(f"Sizga kirish {price} so'm")
