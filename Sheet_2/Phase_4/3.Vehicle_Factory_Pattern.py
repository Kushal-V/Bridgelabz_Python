class Tesla:
    def drive(self):
        print("This is an Electric car (Tesla)")

class Toyota:
    def drive(self):
        print("This is an Gas car (Toyota)")

class VehicleFactory:
    def get_vehicle(self, vehicle_type):
        if vehicle_type == "Electric":
            return Tesla()
        elif vehicle_type == "Gas":
            return Toyota()
        else:
            raise ValueError("Invalid vehicle type")

factory = VehicleFactory()
vehicle1 = factory.get_vehicle("Electric")
vehicle2 = factory.get_vehicle("Gas")
vehicle1.drive()
vehicle2.drive()