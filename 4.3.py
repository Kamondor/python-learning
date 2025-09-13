#nothing to see here
yosh = int(input('Yoshingiz nechida?\n'))
if yosh<=3:
    price = 0
elif yosh<=12:
    price = 3000
elif yosh <65:
    price = 10000
elif yosh >=60:
    price = 8000
print(f"Sizga kirish {price} so'm")
