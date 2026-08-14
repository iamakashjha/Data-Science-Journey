class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def fare(self):
        base_fare = 100
        total_fare = base_fare + (self.capacity * 10)
        return total_fare


bus_1 = bus("School Volvo", 180, 12, 50)
print(f"Bus Name: {bus_1.name}")

bus_fare = bus_1.fare()
print(f"Bus Fare: {bus_fare}")

bus_2 = bus("City Bus", 150, 10, 30)
print(f"\nBus Name: {bus_2.name}")
bus_fare_2 = bus_2.fare()
print(f"Bus Fare: {bus_fare_2}")