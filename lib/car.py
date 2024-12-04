from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
        # Call the __init__ method of the parent class to set up wheel_size and wheel_number
        super().__init__(wheel_size, wheel_number)

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
