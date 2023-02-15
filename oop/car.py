class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year, miles=0):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles


car = Car('subaru', 'outback', 2013, 100)
print(car.miles)
