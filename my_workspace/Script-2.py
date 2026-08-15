from datetime import datetime
import pytz

# Time zones
zones = {
    "IND": "Asia/Kolkata",
    "Newyork": "America/New_York",
    "Australia": "Australia/Sydney",
}

for label, zone in zones.items():
    dt = datetime.now(pytz.timezone(zone))
    print(f"{label}: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
