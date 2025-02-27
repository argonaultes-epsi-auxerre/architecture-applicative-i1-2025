import random

class Probe:

    def get_temperature(self):
        return random.randint(-10, 40)

    def get_humidity(self):
        return random.randint(0, 100)

    def get_pressure(self):
        return random.randint(800, 1100)


class CurrentDisplay:

    def update_current(self, temperature, humidity, pressure):
        print(f'Display current {temperature}, {humidity}, {pressure}')

class ForecastDisplay:

    def update_forecast(self, temperature, humidity, pressure):
        print(f'Display forecast {temperature}, {humidity}, {pressure}')

class StatisticsDisplay:

    def update_statistics(self, temperature, humidity, pressure):
        print(f'Display statistics {temperature}, {humidity}, {pressure}')


class WeatherData:

    def __init__(self, probe : Probe, current_conditions_display: CurrentDisplay, statistics_display: StatisticsDisplay, forecast_display: ForecastDisplay):
        self.__probe = probe
        self.__current_conditions_display = current_conditions_display
        self.__statitics_display = statistics_display
        self.__forecast_display = forecast_display


    def measurements_changed(self):
        temperature = self.__probe.get_temperature()
        humidity = self.__probe.get_humidity()
        pressure = self.__probe.get_pressure()
        self.__current_conditions_display.update_current(temperature, humidity, pressure)
        self.__statitics_display.update_statistics(temperature, humidity, pressure)
        self.__forecast_display.update_forecast(temperature, humidity, pressure)