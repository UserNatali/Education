class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def get_temperature(self):
        return self.temperature

    @get_temperature.setter
    def get_temperature(self, newTemperature):
        self.temperature = newTemperature


temp = Temperature(78)
print("temperature in Fahrenheit", temp.get_temperature * 9 / 5 + 32 )
temp.temperature = 15
print("temperature in Celsius", temp.get_temperature)
