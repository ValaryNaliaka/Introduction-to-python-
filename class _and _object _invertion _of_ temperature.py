#class and object invertion of temperature
class Temperature:
    def __init__(self,temperature):
        self.temperature=temperature
    def convert_celsius(self):
        convert_celsius=((9*self.temperature)/5+32)
        print("temperature in celsius",convert_celsius)
    def convert_fahrenheit(self):
        convert_fahrenheit=((self.temperature-32)*5/9)
        print("temperature in fahrenheit",convert_fahrenheit)
degree=Temperature(70)
degree.convert_celsius()
degree.convert_fahrenheit()
