import csv
import datetime
import os

def export_to_csv(data):
    if not data:
        print("No data available for export.")
        return
    
    filename = f"tyre_data_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    file_path = os.path.join("output", filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    field_names = set()
    for entry in data:
        field_names.update(key for key in entry.keys() if key != '_id')
    field_names = sorted(field_names)  # Sort field names for consistent order

    with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names, restval="N/A")
        writer.writeheader()
        for entry in data:
            if "_id" in entry.keys():
                entry.pop("_id")
            writer.writerow(entry)

    print(f"Data exported successfully to {file_path}")
        
    