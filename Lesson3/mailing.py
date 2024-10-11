from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Путь {self.track} из {self.from_address} "
                f"в {self.to_address}. Стоимостью {self.cost} рублей.")