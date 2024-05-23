class House:  # создание класса

    def __init__(self, number_of_floors=0):
        # (self, number_of_floors=0) - параметры функции
        self.floors = number_of_floors  # атрибут экземпляра класса

    def set_new_number_of_floors(self, floor=1):  # метод класса
        self.floors += 1
        print(self.floors)


house1 = House()  # создание экземпляра

house1.set_new_number_of_floors()