class Vehicle:
    def __init__(self, vehicle_type):
        self.type = vehicle_type

    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")