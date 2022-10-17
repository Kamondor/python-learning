yosh = int(input('Yoshingiz nechida?\n'))
if yosh<=4 or yosh>=60:
    print('Sizga kirish bepul')
elif yosh<18 and yosh>4:
    print('Sizga kirish narxi 10000 so\'m')
elif yosh>18 and yosh<60:
    print('Sizga kirish narxi 20000 so\'m')
    
