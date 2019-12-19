class MechanicalVehicle:
    def __init__(self, l, w, h, c):
        self.length = l
        self.width = w
        self.height = h
        self.color = c

    def Ride(self):
        print("Move")

    def PrintInfo(self):
        print("\nSize: " + str(self.length) + "x" + str(self.width) + "x" + str(self.height))
        print("Color: " + self.color)
            
        

class Car(MechanicalVehicle):
    
    def __init__(self, l, w, h, c, m, mp):
        MechanicalVehicle.__init__(self, l, w, h, c)
        self.model = m
        self.powerOfMotor = mp
        
    def Ride(self):
        print("\nStart engine")
        print("Push gas pedal")


class Bike(MechanicalVehicle):
    def __init__(self, l, w, h, c, m, cw):
        MechanicalVehicle.__init__(self, l, w, h, c)
        self.model = m
        self.countOfWheels = cw

    def Ride(self):
        print("\nHold steering wheel")
        print("Push pedals")


class MotoBike(MechanicalVehicle):
    def __init__(self, l, w, h, c, m, cw, mp):
        MechanicalVehicle.__init__(self, l, w, h, c)
        self.model = m
        self.countOfWheels = cw
        self.powerOfMotor = mp

    def Ride(self):
        print("Hold steering wheel")
        print("Start engine")
        print("Push gas pedal")
        

car = Car(4, 2, 1.5, 'black', "BMW", 400)
bike = Bike(2, 0.45, 0.5, 'gray', 'BMX', 2)
motobike = MotoBike(2, 0.75, 0.68, 'red', "Harley", 2, 150)

print('-----------Car-----------')
car.PrintInfo()
car.Ride()
print('-----------Bike-----------')
bike.PrintInfo()
bike.Ride()
print('-----------MotoBike-----------')
motobike.PrintInfo()
motobike.Ride()



