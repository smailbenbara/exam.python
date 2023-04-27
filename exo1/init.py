class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), {self.color}"