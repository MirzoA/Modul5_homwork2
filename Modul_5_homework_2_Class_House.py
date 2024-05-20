class House:  # создание класса

    def __init__(self, number_of_floors=0):
        # (self, number_of_floors=0) - параметры функции
        self.floors = number_of_floors  # атрибут экземпляра класса

    def setNewNumberOfFloors(self, floor=1):  # метод класса
        self.floors += 1
        print(self.floors)


house1 = House()  # создание экземпляра

house1.setNewNumberOfFloors()