foydalanuvchilar = ['Kamondor', 'krisa_n1', 'Professor41k', 'Rampage', 'Simple_top', 'TT_Proboy']
new_login = input('Yangi loginni kiriting: ')
for solishtirish in foydalanuvchilar:
    if new_login in foydalanuvchilar:
        foydalanuvchilar.append(new_login)
        print(f"Xush kelibsiz, {new_login}!")
    else:
        print('Login band')
