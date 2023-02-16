
class DistanceMixin:
    """Convert distances from metric to imperial (and reverse)"""

    def km_to_miles(self, km):
        """Convert kilometers to miles"""
        return km * 0.621371

    def miles_to_km(self, miles):
        """Convert miles to kilometers"""
        return miles / 0.621371

    def class_name(self):
        return 'DistanceMixin'


class TempMixin:
    """Convert temperatues from metric to imperial (and reverse)"""

    def f_to_c(self, f):
        """Convert fahrenheit to celsius"""
        return (f - 32) * 5 / 9

    def c_to_f(self, c):
        """Convert celsius to fahrenheit"""
        return c * 9 / 5 + 32

    def class_name(self):
        return 'TempMixin'


class DigitalStorageMixin:
    """Convert digital storage from metric to imperial (and reverse)"""

    def mb_to_gb(self, mb):
        """Convert megabytes to gigabytes"""
        return mb / 1000

    def gb_to_mb(self, gb):
        """Convert gigabytes to megabytes"""
        return gb * 1000

    def class_name(self):
        return 'DigitalStorageMixin'


class Weather(TempMixin, DistanceMixin, DigitalStorageMixin):
    """A class to convert weather data from metric to imperial (and reverse)"""

    def __init__(self, celcius, kmph):
        """Initialize attributes to describe a weather data"""
        self._celcius = celcius
        self._kmph = kmph

    def display(self, metric=True):
        """Display the weather data"""
        if metric:
            temp = self._celcius
            wind = self._kmph
        else:
            temp = self.c_to_f(self._celcius)
            wind = self.km_to_miles(self._kmph)

        print(f'Temperature: {temp}')
        print(f'Wind speed: {wind}')


london = Weather(12, 7)
london.display(metric=False)
print(london.class_name())


class HardDrive(DigitalStorageMixin, TempMixin):
    def __init__(self, mb, celsius):
        self._mb = mb
        self._celsius = celsius

    def display(self, metric=True):
        if metric:
            temp = self._celsius
        else:
            temp = self.c_to_f(self._celsius)

        print(f'Temperature: {temp}')
        print(f'Size: {self.mb_to_gb(self._mb)} GB')
