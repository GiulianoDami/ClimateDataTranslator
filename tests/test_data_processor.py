import unittest
from data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor()

    def test_convert_temperature_anomaly(self):
        result = self.processor.convert_temperature_anomaly(0.87)
        self.assertEqual(result, "Global temperatures have risen 0.87°C")

    def test_convert_co2_concentration(self):
        result = self.processor.convert_co2_concentration(415.2)
        self.assertEqual(result, "Atmospheric CO2 concentration is 415.2 ppm")

    def test_convert_sea_level_rise(self):
        result = self.processor.convert_sea_level_rise(3.3)
        self.assertEqual(result, "Sea levels are rising at a rate of 3.3 mm/year")

    def test_generate_summary(self):
        data = {
            'temperature_anomaly': 0.87,
            'co2_concentration': 415.2,
            'sea_level_rise': 3.3
        }
        summary = self.processor.generate_summary(data)
        expected_summary = (
            "Global temperatures have risen 0.87°C\n"
            "Atmospheric CO2 concentration is 415.2 ppm\n"
            "Sea levels are rising at a rate of 3.3 mm/year"
        )
        self.assertEqual(summary, expected_summary)

if __name__ == '__main__':
    unittest.main()