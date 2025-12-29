import pandas as pd

class DataProcessor:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def summarize_temperature(self):
        anomaly = self.data['Temperature Anomaly'].mean()
        return f"Global temperatures have risen {anomaly:.2f}°C above the baseline (1951-1980)."

    def summarize_co2(self):
        concentration = self.data['CO2 Concentration'].mean()
        return f"The average CO2 concentration is {concentration:.1f} ppm."

    def summarize_sea_level(self):
        rise = self.data['Sea Level Rise'].mean()
        return f"Sea levels are rising at a rate of {rise:.1f} mm/year."

    def generate_summary(self):
        temperature_summary = self.summarize_temperature()
        co2_summary = self.summarize_co2()
        sea_level_summary = self.summarize_sea_level()
        return f"{temperature_summary}\n{co2_summary}\n{sea_level_summary}"

    def save_summary(self, output_path):
        summary = self.generate_summary()
        with open(output_path, 'w') as file:
            file.write(summary)