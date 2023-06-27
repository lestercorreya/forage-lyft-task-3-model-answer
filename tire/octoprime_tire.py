from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        if sum(self.sensor_array) >= 3:
            return True
        else:
            return False