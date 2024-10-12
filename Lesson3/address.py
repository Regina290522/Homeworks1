class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return (f"{self.index}, "
                f"{self.city}, "
                f"{self.street}, "
                f"{self.house} - "
                f"{self.apartment}")
