import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_anomalies(data, baseline_start, baseline_end):
    baseline = data[(data['Year'] >= baseline_start) & (data['Year'] <= baseline_end)]
    mean_baseline = baseline.mean()
    data['Anomaly'] = data - mean_baseline
    return data

def generate_summary(data):
    summary = []
    for index, row in data.iterrows():
        year = row['Year']
        temp_anomaly = row['Temperature Anomaly']
        co2_concentration = row['CO2 Concentration']
        sea_level_rise = row['Sea Level Rise']
        
        summary.append(f"In {year}, global temperatures were {temp_anomaly:.2f}°C above the baseline.")
        summary.append(f"Carbon dioxide levels reached {co2_concentration} ppm.")
        summary.append(f"Sea levels rose by {sea_level_rise:.2f} mm/year.")
        summary.append("")
    
    return "\n".join(summary)

def create_visualization(data, column_name, title):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data[column_name], label=column_name)
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel(column_name)
    plt.legend()
    plt.grid(True)
    plt.show()

def add_source_attribution(summary, source):
    return f"{summary}\n\nSource: {source}"