car = {
    'make':'gm',
    'model':'Malibu',
    'color':'black',
    'gear':'automatic',
    'year':'2022',
    'price':'40000$'

    }
narx = car.get('narx', 'Bunday kalit mavjud emas') # Narx so'ralganda mavjud ems deydi
print(car['model'])
car['key'] = 'value' # Key and value appends
del car['color'] # Delete key and value
car['model'] = 'gentra'
print(narx)
print(car['model'])
