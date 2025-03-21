class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def get_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life} hours"