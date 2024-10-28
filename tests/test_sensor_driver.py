
import unittest
from firmware import sensor_driver

class TestSensorDriver(unittest.TestCase):
    def test_temperature_reading(self):
        temp = sensor_driver.SensorDriver.readTemperature()
        self.assertTrue(-40 <= temp <= 80)  # Valid temperature range

if __name__ == "__main__":
    unittest.main()
