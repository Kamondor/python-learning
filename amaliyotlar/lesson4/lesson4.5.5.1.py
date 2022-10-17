foydalanuvchilar = ['Kamondor', 'krisa_n1', 'Professor41k', 'Rampage', 'Simple_top', 'TT_Proboy']
new_login = input('Yangi loginni kiriting: ')
list_1 = []
list_1.append(new_login)
for n in list_1:
    if n in foydalanuvchilar:
        print('Login band, boshqa login tanlang')
    else:
        foydalanuvchilar.append(new_login)
        print(f"Xush kelibsiz, {new_login}!")
