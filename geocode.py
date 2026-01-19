import argparse
import requests
import time
import os

HEADERS = {
    "User-Agent": "map-select-geocoder/1.0 (contact: gui@toruscare.com)"
}

# ViewBox/map transform constants for lat/lon <-> SVG x/y conversion
minLon = 97.344728
maxLat = 20.463430
maxLon = 105.640023
minLat = 5.614417
vbW = 559.57092
vbH = 1024.7631
lonSpan = maxLon - minLon
latSpan = maxLat - minLat

# Address groups: (label, [candidate queries])
address_groups = [
    ("Kumphawapi Hospital (Udon Thani)", [
        "Kumphawapi Hospital, Kumphawapi, Udon Thani, Thailand",
        "Kumphawapi Hospital, Udon Thani, Thailand",
        "โรงพยาบาลกุมภวาปี, Udon Thani, Thailand",
    ]),
    ("Kaengkhro / Kaeng Khro Hospital (Chaiyaphum)", [
        "Kaeng Khro Hospital, Kaeng Khro, Chaiyaphum, Thailand",
        "Kaengkhro Hospital, Chaiyaphum, Thailand",
        "โรงพยาบาลแก้งคร้อ, Chaiyaphum, Thailand",
    ]),
    ("King Chulalongkorn Memorial Hospital (Bangkok)", [
        "King Chulalongkorn Memorial Hospital, Rama IV, Pathum Wan, Bangkok, Thailand",
        "King Chulalongkorn Memorial Hospital, Bangkok, Thailand",
    ]),
    ("The Blessing Nursing Home & Rehab (Bangkok)", [
        "The Blessing Nursing Home & Rehab, Prawet, Bangkok, Thailand",
        "The Blessing Nursing Home, Srinagarindra, Prawet, Bangkok, Thailand",
        "Blessing Nursing Home Bangkok 10250",
    ]),
    ("Khlong Thom Hospital (Krabi)", [
        "Khlong Thom District, Krabi, Thailand",
        "Phetkasem Road, 81120",
    ])
]

url = "https://nominatim.openstreetmap.org/search"


def geocode_query(q):
    params = {"format": "json", "q": q, "limit": 1}
    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=10)
    except Exception as e:
        return None, None, f"request-error: {e}"

    if resp.status_code != 200:
        return None, None, f"http-{resp.status_code}"

    if "application/json" not in resp.headers.get("Content-Type", ""):
        return None, None, "non-json-response"

    data = resp.json()
    if not data:
        return None, None, "no-data"

    return float(data[0]["lat"]), float(data[0]["lon"]), data[0].get("display_name", "")


def latlon_to_xy(lat, lon):
    x = (lon - minLon) * (vbW / lonSpan)
    y = (maxLat - lat) * (vbH / latSpan)
    return round(x, 3), round(y, 3)


def append_to_compute(coords, path="coordinates.txt"):
    # Append found coordinates to a simple CSV-like file: lat,lon,label
    created = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if created:
            f.write("# Appended by geocode.py (lat,lon,label)\n")
        for lat, lon, name in coords:
            f.write(f"{lat},{lon},{name}\n")
    print(f"Appended {len(coords)} entries to {path}")


def main(append=False, out='coordinates.txt'):
    found_list = []
    for label, candidates in address_groups:
        print(f"Group: {label}")
        found = False
        for q in candidates:
            print(f" Query: {q}")
            lat, lon, info = geocode_query(q)
            print(f"  Result: {info}")
            if lat is not None:
                print(f"  FOUND: {lat}, {lon} -> {info}")
                found = True
                found_list.append((lat, lon, label))
                break
            time.sleep(1.1)

        if not found:
            print(" No coordinates found for this group.")
        print("---")
        time.sleep(1.1)

    if append and found_list:
        # append found coords to the specified output file in CSV format
        append_to_compute(found_list, path=out)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Geocode address groups and optionally append results to a file')
    p.add_argument('--append', action='store_true', help='Append found lat/lon tuples to a local file (default: coordinates.txt)')
    p.add_argument('--out', default='coordinates.txt', help='Output file to append results to when using --append')
    args = p.parse_args()
    main(append=args.append, out=args.out)
