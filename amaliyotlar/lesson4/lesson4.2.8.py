#number = int(input("Istalgan sonni kiriting: "))
#if number >=0:
#    print('Musbat son')
#else:
#   print('Manfiy son')
number = int(input("Istalgan sonni kiriting: "))
if number >= 0:
    sqrt_number = number**(1/2)
    print(f"{number} ning kvadrat ildizi {sqrt_number} ga teng ")
else:
    print('Musbat son kiriting')
