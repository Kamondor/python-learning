a = int(input('1-sonni kiriting:\n'))
b = int(input('2-sonni kiriting:\n'))
mehmonlar = ['Ali', 'Vali', 'Soli', 'Olim', 'Hasan', 'Husan']

sonlar = list(range(a,b))
for mehmon in mehmonlar:
    print(mehmon)

for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}")
    print(f"Sizni 20-mart kuni nahorgi oshga taklif qilamiz.")
    print("Hurmat bilan Palonchiyevlar oilasi")

for son in sonlar:
    print(f"{son}ning kvadrati {son**2} ga teng")


