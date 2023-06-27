from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        if any(value > 0.9 for value in self.sensor_array):
            return True
        else:
            return False