import unittest
from Assignment4_KF import get_forecast_data

class TestWeather(unittest.TestCase):

    def test_periods_list(self):
        #Test that periods is a list of at least 14 objects
        forecast_json = get_forecast_data()
        periods = forecast_json["properties"]["periods"]
        self.assertIsInstance(periods, list)
        self.assertGreaterEqual(len(periods), 14)

    def test_period_keys(self):
        #Test that each forecast period has required keys
        forecast_json = get_forecast_data()
        periods = forecast_json["properties"]["periods"]
        first = periods[0]
        self.assertIn("name", first)
        self.assertIn("temperature", first)
        self.assertIn("detailedForecast", first)

if __name__ == '__main__':
    unittest.main()
