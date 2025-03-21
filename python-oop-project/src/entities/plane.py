class Vehicle:
    def __init__(self, vehicle_type):
        self.type = vehicle_type

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Plane(Vehicle):
    def __init__(self, model, capacity):
        super().__init__("Plane")
        self.model = model
        self.capacity = capacity

    def move(self):
        return "Flying ✈️"

    def get_info(self):
        return f"Model: {self.model}, Capacity: {self.capacity} passengers"