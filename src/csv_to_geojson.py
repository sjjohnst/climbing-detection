import csv
import json

def csv_to_geojson(csv_path, geojson_path):
    features = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(row["longitude"]), float(row["latitude"])]
                },
                "properties": {
                    "name": row["name"],
                    "description": row["description"]
                }
            }
            features.append(feature)
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    with open(geojson_path, "w", encoding='utf-8') as f:
        json.dump(geojson, f, indent=2)

if __name__ == "__main__":
    csv_to_geojson("data/pins/all_boulders.csv", "data/pins/all_boulders.geojson")