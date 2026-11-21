import csv
import io
import sqlite3

print("--- TASK B1: Cleaning Pipeline ---")

RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Adyar,2026-10-04,1050
"""

def load_clean(text):
    """Returns (station, date, pm25) tuples for valid, non-negative readings only."""
    rows = []
    f = io.StringIO(text.strip())
    reader = csv.DictReader(f)
    for row in reader:
        val = row['pm25'].strip()
        if val and val != 'NA':
            try:
                pm_val = float(val)
                # Added check to skip values above 999 as per instructions
                if 0 <= pm_val <= 999:
                    rows.append((row['station'], row['date'], pm_val))
            except ValueError:
                continue
    return rows

def min_max(values):
    if not values:
        return []
    v_min = min(values)
    v_max = max(values)
    if v_max == v_min:
        return [0.0 for _ in values]
    return [round((v - v_min) / (v_max - v_min), 3) for v in values]

clean_data = load_clean(RAW)
print("Cleaned Data:", clean_data)
print("Min-Max Scaled PM2.5:", min_max([pm for _, _, pm in clean_data]))
print("\n")


# ==========================================
# TASK B2: SQL DATABASE & INJECTION PROTECTION
# ==========================================
print("--- TASK B2: SQL Implementation ---")

readings = [("Adyar", "2026-10-01", 48.0), ("Guindy", "2026-10-01", 95.0),
            ("Guindy", "2026-10-03", 121.0), ("Adyar", "2026-10-04", 60.0)]

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE aq (station TEXT, day TEXT, pm25 REAL)")

# Using executemany with ? placeholders for security
con.executemany("INSERT INTO aq VALUES (?, ?, ?)", readings)
con.commit()

def station_average(name):
    # Using parameterized SELECT to prevent SQL injection
    cursor = con.execute("SELECT AVG(pm25) FROM aq WHERE station = ?", (name,))
    result = cursor.fetchone()[0]
    return result

print(f"Adyar Average: {station_average('Adyar')}")
print(f"Guindy Average: {station_average('Guindy')}")
print(f"Injection Attempt Result: {station_average(\"Adyar' OR '1'='1\")}") 
con.close()
print("\n")


print("--- TASK B4: AI Sentiment Scorer ---")

POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}

def score(text):
    """+1 per positive word, -1 per negative word; a preceding negator flips it."""
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0
    prev_is_negator = False
    
    for word in words:
        word_val = 0
        if word in POSITIVE:
            word_val = 1
        elif word in NEGATIVE:
            word_val = -1
            
        if word_val != 0:
            if prev_is_negator:
                word_val *= -1
            total += word_val
            
        prev_is_negator = word in NEGATORS
        
    return total

def label(text):
    s = score(text)
    return "positive" if s > 0 else "negative" if s < 0 else "neutral"

complaints = [
    "Roads are clean and the bus was fast.",
    "Smoke from the factory, air is bad.",
    "The staff were not helpful.",
    "Not bad, service improved."
]

for c in complaints:
    print(f"{label(c):8} | {c}")
