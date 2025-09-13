menyu = ['plov', 'qozonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?')
ovqat = ovqat.title()
if ovqat.lower() in menyu:
    print('Buyurtma qabul qilindi')
else:
    print('Afsuski, bizda bunday ovqat yo\'q')
    

print('manti' in menyu)
print('osh' not in menyu)
