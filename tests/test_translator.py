import unittest
from climate_translator import ClimateDataTranslator

class TestClimateDataTranslator(unittest.TestCase):

    def setUp(self):
        self.translator = ClimateDataTranslator()

    def test_temperature_anomaly_translation(self):
        data = {"Temperature anomaly": "0.87°C above baseline (1951-1980)"}
        expected_output = "Global temperatures have risen 0.87°C"
        self.assertEqual(self.translator.translate(data), expected_output)

    def test_co2_concentration_translation(self):
        data = {"CO2 concentration": "415.2 ppm"}
        expected_output = "Atmospheric CO2 levels are at 415.2 parts per million"
        self.assertEqual(self.translator.translate(data), expected_output)

    def test_sea_level_rise_translation(self):
        data = {"Sea level rise": "3.3 mm/year"}
        expected_output = "Sea levels are rising at a rate of 3.3 millimeters per year"
        self.assertEqual(self.translator.translate(data), expected_output)

    def test_multiple_data_points_translation(self):
        data = {
            "Temperature anomaly": "0.87°C above baseline (1951-1980)",
            "CO2 concentration": "415.2 ppm",
            "Sea level rise": "3.3 mm/year"
        }
        expected_output = (
            "Global temperatures have risen 0.87°C\n"
            "Atmospheric CO2 levels are at 415.2 parts per million\n"
            "Sea levels are rising at a rate of 3.3 millimeters per year"
        )
        self.assertEqual(self.translator.translate(data), expected_output)

if __name__ == '__main__':
    unittest.main()