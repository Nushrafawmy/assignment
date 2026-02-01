
import csv

input_file = "sales-data.csv"
output_file = "below_avg_price_per_sqft.csv"

rows = []
ppsf_values = []

with open(input_file, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["sq__ft"]) > 0:
            ppsf = int(row["price"]) / int(row["sq__ft"])
            row["ppsf"] = ppsf
            rows.append(row)
            ppsf_values.append(ppsf)

avg = sum(ppsf_values) / len(ppsf_values)

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    for r in rows:
        if r["ppsf"] < avg:
            writer.writerow(r)

print("Generated:", output_file)
