""" This example shows usage of properties feature in Python.
In general properties are interface to instance variables (specially to private instance attributes).
 Property should not be used as replacement for general methods - then the code would suffers from legibility.
 Property can define only getter for private variable that should be externally prevented from setting.
 Also, can be used are as only setter (less commonly) when attribute is intended to be externally set but not read.
 Although more frequently used is as setter and getter in parallel."""


class Temperature(object):
    def __init__(self):
        # temperature as private attribute - cannot be accessed in standard way outside class
        self.__temperature = None

    def to_fahrenheit(self):
        return self.__temperature * 1.8 + 32

    @property
    def temperature(self):
        print("Getting temperature %d" % self.__temperature)
        return self.__temperature

    @temperature.setter
    def temperature(self, temp):
        if temp < -273:
            raise AttributeError("Temperature should not be less than absolute zero")
        print("Setting temperature: %d" % temp)
        self.__temperature = temp


if __name__ == "__main__":
    t = Temperature()
    try:
        t.temperature = -280
    except AttributeError:
        print("Temperature cannot be less than absolute zero - -273 C degree")

    t.temperature = -10
