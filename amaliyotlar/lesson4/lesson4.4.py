menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['PLov', 'somsa', 'manti', 'shashlik']

for taom in buyurtmalar:
    if taom in menyu:
        print(f"Menyuda {taom} bor")
    else:
        print(f"Kechirasiz, menyuda {taom} yo'q")
