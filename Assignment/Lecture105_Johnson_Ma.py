class vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on: Air")
        
class car(vehicle):
    pass
class pickUp(vehicle):
    pass
class van(vehicle):
    pass
class estateCar(vehicle):
    pass

car1 = car()
car1.turnOnAirConditioner()

pickUp1 = pickUp()
pickUp1.turnOnAirConditioner()

van1 = van()
van1.turnOnAirConditioner()

estateCar1 = estateCar()
estateCar1.turnOnAirConditioner()