import geojson
import pandas as pd
import argparse
from datetime import datetime

def convert_unix_to_datetime(unix_time):
    return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')

def extract_features(geojson_data):
    return [
        {
            'longitude': feature['geometry']['coordinates'][0],
            'latitude': feature['geometry']['coordinates'][1],
            'altitude_m': feature['geometry']['coordinates'][2],
            'time': convert_unix_to_datetime(feature['properties'].get('time', 0)),
            'gpheight_m': feature['properties'].get('gpheight'),
            'temperature_K': feature['properties'].get('temp'),
            'dewpoint_K': feature['properties'].get('dewpoint'),
            'pressure_hPa': feature['properties'].get('pressure'),
            'wind_u_m_s': feature['properties'].get('wind_u'),
            'wind_v_m_s': feature['properties'].get('wind_v')
        }
        for feature in geojson_data.get('features', [])
    ]

def main():
    parser = argparse.ArgumentParser(description='Extract meteorological data from GeoJSON to CSV.')
    parser.add_argument('input_file', help='Path to input GeoJSON file')
    parser.add_argument('output_file', help='Path to output CSV file')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            data = geojson.load(f)
    except Exception as e:
        print(f"Error reading GeoJSON file: {e}")
        return

    records = extract_features(data)
    df = pd.DataFrame(records)

    try:
        df.to_csv(args.output_file, index=False, encoding='utf-8-sig')
        print(f"Data successfully saved to {args.output_file}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")

if __name__ == '__main__':
    main()