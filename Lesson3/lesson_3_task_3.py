from address import Address
from mailing import Mailing

to_address = Address ("123@mail.ru", "456@mail.ru", "789@mail.ru", "135@mail.ru", "246@mail.ru"),
from_address = Address ("abc@yandex.ru", "dfg@yandex.ru", "hjk@yandex.ru", "lmn@yandex.ru", "opq@yandex.ru"),
mailing = Mailing(to_address, from_address, 1300, "dress123")
print(mailing)
