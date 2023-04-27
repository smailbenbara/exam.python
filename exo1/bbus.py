from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand, model, year, color, capacity):
        super().__init__(brand, model, year, color)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()}, {self.capacity} passengers"
