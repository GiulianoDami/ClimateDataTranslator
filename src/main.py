import argparse
import pandas as pd

def translate_data(input_file, output_file, format_type):
    # Load data from CSV
    data = pd.read_csv(input_file)
    
    # Create a plain text summary
    if format_type == 'plain':
        summary = create_plain_summary(data)
    else:
        raise ValueError("Unsupported format type")
    
    # Write summary to output file
    with open(output_file, 'w') as f:
        f.write(summary)

def create_plain_summary(data):
    summary = []
    for index, row in data.iterrows():
        temp_anomaly = row.get('Temperature anomaly', 'N/A')
        co2_concentration = row.get('CO2 concentration', 'N/A')
        sea_level_rise = row.get('Sea level rise', 'N/A')
        
        if temp_anomaly != 'N/A':
            summary.append(f"Global temperatures have risen {temp_anomaly}°C above the baseline (1951-1980)")
        if co2_concentration != 'N/A':
            summary.append(f"Atmospheric CO2 levels are at {co2_concentration} ppm")
        if sea_level_rise != 'N/A':
            summary.append(f"Sea levels are rising at a rate of {sea_level_rise} mm/year")
    
    return "\n".join(summary)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate climate data into plain English summaries.")
    parser.add_argument("--input", required=True, help="Path to the input CSV file containing climate data.")
    parser.add_argument("--output", required=True, help="Path to the output file where the summary will be saved.")
    parser.add_argument("--format", default='plain', choices=['plain'], help="Format type for the summary (currently only 'plain' is supported).")
    
    args = parser.parse_args()
    translate_data(args.input, args.output, args.format)