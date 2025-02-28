import random

from abc import ABC, abstractmethod

class Probe:

    def get_temperature(self):
        return random.randint(-10, 40)

    def get_humidity(self):
        return random.randint(0, 100)

    def get_pressure(self):
        return random.randint(800, 1100)

class Display(ABC):

    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

class CurrentDisplay(Display):

    def update(self, temperature, humidity, pressure):
        print(f'Display current {temperature}, {humidity}, {pressure}')

class ForecastDisplay(Display):

    def update(self, temperature, humidity, pressure):
        print(f'Display forecast {temperature}, {humidity}, {pressure}')

class StatisticsDisplay(Display):

    def update(self, temperature, humidity, pressure):
        print(f'Display statistics {temperature}, {humidity}, {pressure}')


class WeatherData:

    def __init__(self, probe : Probe, current_conditions_display: CurrentDisplay, statistics_display: StatisticsDisplay, forecast_display: ForecastDisplay):
        self.__probe = probe
        self.__displays = []
        self.__displays.append(current_conditions_display)
        self.__displays.append(statistics_display)
        self.__displays.append(forecast_display)
        self.__temperature = None
        self.__humidity = None
        self.__pressure = None

    def add_display(self, display: Display):
        self.__displays.append(display)


    def measurements_changed(self):
        self.__temperature = self.__probe.get_temperature()
        self.__humidity = self.__probe.get_humidity()
        self.__pressure = self.__probe.get_pressure()
        self.notify()
    
    def notify(self):
        for display in self.__displays:
            display.update(self.__temperature, self.__humidity, self.__pressure)



if __name__ == '__main__':
    weather_data = WeatherData(Probe(), CurrentDisplay(), StatisticsDisplay(), ForecastDisplay())

    weather_data.measurements_changed()

    new_big_screen = StatisticsDisplay()

    weather_data.add_display(new_big_screen)

    weather_data.measurements_changed()