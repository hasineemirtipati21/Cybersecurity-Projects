import pandas as pd

data = pd.read_csv(
    "traffic_data.csv",
    names=["Source","Destination","Protocol","Size"]
)

print("\nTop Source IPs:")
top_sources = data["Source"].value_counts()
print(top_sources.head())

print("\nProtocol Usage:")
print(data["Protocol"].value_counts())

# Suspicious Traffic Detection
print("\nChecking for suspicious activity...")

for ip, count in top_sources.items():
    if count > 50:
        print(f"⚠ ALERT: Suspicious traffic detected from {ip} ({count} packets)")