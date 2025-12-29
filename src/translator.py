import pandas as pd

class ClimateDataTranslator:
    def __init__(self, input_file):
        self.data = pd.read_csv(input_file)

    def translate(self, output_format='plain'):
        summaries = []
        for index, row in self.data.iterrows():
            temperature_anomaly = row.get('Temperature anomaly', None)
            co2_concentration = row.get('CO2 concentration', None)
            sea_level_rise = row.get('Sea level rise', None)

            if temperature_anomaly is not None:
                summaries.append(f"Global temperatures have risen {temperature_anomaly}°C above the baseline (1951-1980).")

            if co2_concentration is not None:
                summaries.append(f"Atmospheric CO2 levels are currently at {co2_concentration} ppm.")

            if sea_level_rise is not None:
                summaries.append(f"Sea levels are rising at a rate of {sea_level_rise} mm/year.")

        if output_format == 'plain':
            return '\n'.join(summaries)
        elif output_format == 'html':
            return '<br>'.join(summaries)
        else:
            raise ValueError("Unsupported output format. Use 'plain' or 'html'.")

    def save_summary(self, output_file, output_format='plain'):
        summary = self.translate(output_format)
        with open(output_file, 'w') as file:
            file.write(summary)