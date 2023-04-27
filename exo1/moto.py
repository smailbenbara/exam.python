from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, engine_type):
        super().__init__(brand, model, year, color)
        self.engine_type = engine_type

    def __str__(self):
        return f"{super().__str__()}, {self.engine_type} engine"