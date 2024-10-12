from address import Address
from mailing import Mailing


to_address = Address("843", "Казань", "Баумана", "246", "1")
from_address = Address("950", "Москва", "Садовая", "393", "2")

mailing = Mailing(to_address, from_address, 1300, "поезда")

part1 = (f"Отправление {mailing.track} "
         f"из {mailing.from_address.index}, "
         f"{mailing.from_address.city}, "
         f"{mailing.from_address.street}, "
         f"{mailing.from_address.house} - {mailing.from_address.apartment}")
part2 = (f"в {mailing.to_address.index}, "
         f"{mailing.to_address.city}, "
         f"{mailing.to_address.street}, "
         f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
         f"Стоимость  {mailing.cost} рублей.")
print(part1)
print(part2)
