class Ride:

    surge_multiplier = 1.5

    def __init__(self,base_fare,per_mile_rate):
        self.base_fare = base_fare
        self.per_mile_rate = per_mile_rate

    def calculate_fare(self,miles):
        return (self.base_fare + self.per_mile_rate * miles) * self.surge_multiplier
    
    @classmethod
    def set_surge_multiplier(cls,multiplier):
        cls.surge_multiplier = multiplier

class UberX(Ride):
    def __init__(self):
        super().__init__(base_fare=10, per_mile_rate=2)

class UberBlack(Ride):
    def __init__(self):
        super().__init__(base_fare=20, per_mile_rate=3)

class UberPool(Ride):
    def __init__(self):
        super().__init__(base_fare=30, per_mile_rate=4)


ride1 = UberX()
ride2 = UberBlack()
ride3 = UberPool()

print(ride1.calculate_fare(10))
print(ride2.calculate_fare(10))
print(ride3.calculate_fare(10))

Ride.set_surge_multiplier(2)
print(ride1.calculate_fare(10))
print(ride2.calculate_fare(10))
print(ride3.calculate_fare(10))
