foydalanuvchilar = ['Kamondor', 'krisa_n1', 'neo', 'Rampage', 'matrix', 'morphieus']
new_login = input('Yangi loginni kiriting: ')
for solishtirish in foydalanuvchilar:
    if new_login in foydalanuvchilar:
        foydalanuvchilar.append(new_login)
        print(f"Xush kelibsiz, {new_login}!")
    else:
        print('Login band')
