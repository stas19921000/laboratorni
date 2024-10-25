#    i = int(input("Введіть кількість кімнат: "))
#class room:
#    length = 0.0
#    width = 0.0
#    def calculated_area(self): #або перечислити імена змінних
#        self.name = input("Введіть назву: ")
#        self.length = float(input("Введіть довжину: "))
#        self.width = float(input("Введіть ширину: "))
#        print ("Площа", self.name, "=", self.length * self.width)

#for i in range(0, room.i):
#    room1 = room()
#    room1.calculated_area()
    
    
    
class Room:
    def __init__(self, name):
        self.name = name
        self.length = 0.0
        self.width = 0.0

    def input_dimensions(self):
        self.length = float(input(f"Введіть довжину кімнати '{self.name}': "))
        self.width = float(input(f"Введіть ширину кімнати '{self.name}': "))

    def calculate_area(self):
        return self.length * self.width

# Основна програма
try:
    num_rooms = int(input("Введіть кількість кімнат: "))
    for i in range(num_rooms):
        room_name = input(f"Введіть назву кімнати №{i+1}: ")
        room = Room(room_name)
        room.input_dimensions()
        print(f"Площа кімнати '{room.name}' = {room.calculate_area()} кв.м.")
except ValueError:
    print("Помилка: введіть коректні числові значення!")
