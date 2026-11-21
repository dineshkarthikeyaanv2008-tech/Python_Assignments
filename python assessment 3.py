print("--- Q2: Grid and Tuple Results ---")
rows, cols = 3, 4

bad = [[0] * cols] * rows # every row is the SAME list object
bad[0][1] = 7

good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)
print("Are bad rows identical?", bad[0] is bad[1])
print("Are good rows identical?", good[0] is good[1])

# Tuples are immutable, so they can be used as dictionary keys
stops = {(13.0827, 80.2707): "Chennai Central", (13.0418, 80.2341): "T. Nagar"}
print("Stop Lookup:", stops[(13.0418, 80.2341)])
print("\n")


# --- Q3: Dictionaries: Farmer Helpline Complaint Analysis ---
print("--- Q3: Complaint Analysis Results ---")
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    # TODO 1: Return a dictionary word -> count for every word that is not in stop
    counts = {}
    for text in texts:
        words = text.split()
        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    # TODO 2: Return the k most frequent (word, count) pairs, highest count first and alphabetical for ties
    # We use -item[1] for descending count and item[0] for ascending alphabetical order
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

print("Top words:", top(frequencies(calls, STOP), 3))
print("\n")


# --- Q4: Sets: Elective Registration Clash Detection ---
print("--- Q4: Elective Registration Results ---")
ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

# TODO 1: Use set operators to find: students in both, exactly one, and neither
both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

print("clash :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither :", sorted(neither))
