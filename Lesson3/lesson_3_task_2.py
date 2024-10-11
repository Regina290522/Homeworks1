from smartphone import Smartphone

catalog = [
Smartphone("Iphone 11", "64Gb", "+79333333333"),
Smartphone("Iphone 13", "129Gb", "+79345111111"),
Smartphone("Iphone 15", "256Gb", "+79000000000"),
Smartphone("Sumsung", "s24 ultra", "+79456545654"),
Smartphone("Huawei", "pura 70 ultra", "+79809112234")
]
for phone in catalog:
    print(f'Марка:{phone.brand}, Модель {phone.model}, Номер телефона {phone.number}')
