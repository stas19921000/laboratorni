class room:
    length = 0.0
    width = 0.0
    i = int(input("Введіть кількість кімнат: "))
    def calculated_area(self): #або перечислити імена змінних
        self.name = input("Введіть назву: ")
        self.length = float(input("Введіть довжину: "))
        self.width = float(input("Введіть ширину: "))
        print ("Площа", self.name, "=", self.length * self.width)

for i in range(0, room.i):
    room1 = room()
    room1.calculated_area()