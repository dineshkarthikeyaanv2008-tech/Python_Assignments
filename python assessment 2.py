# ==========================================
# Q3 – Vehicle Registration Number Validator
# ==========================================

def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)."""
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
    if len(reg) == 9:
        # Format: LL D D L DDDD
        return reg[0:2].isalpha() and reg[2:4].isdigit() and reg[4:5].isalpha() and reg[5:9].isdigit()
    elif len(reg) == 10:
        # Format: LL D D LL DDDD
        return reg[0:2].isalpha() and reg[2:4].isdigit() and reg[4:6].isalpha() and reg[6:10].isdigit()
    return False

print("--- Q3 Results ---")
for raw in ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB"]:
    reg = normalise(raw)
    print(f"{raw:15} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")
print("\n")


# ==========================================
# Q4 – Building Long Text: + or join()?
# ==========================================

import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    # TODO 1: Build the same text using a single str.join() call
    return ";".join(parts) + ";"

print("--- Q4 Results ---")
start = time.perf_counter(); a = build_plus(items); t_plus = time.perf_counter() - start
start = time.perf_counter(); b = build_join(items); t_join = time.perf_counter() - start
print("same text:", a == b, "| length:", len(b))
print(f"+= time: {t_plus:.4f} s join time: {t_join:.4f} s")
print("\n")


# ==========================================
# Q5 – Functions, Parameters and Scope
# ==========================================

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    # TODO 1: Create a new empty list when order is None, append the item and return the list
    if order is None:
        order = []
    order.append(item)
    return order

print("--- Q5 Results ---")
print("Buggy version (should show shared list):")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print("\nCorrect version (should show independent lists):")
print(add_item("Tea"), add_item("Vada"))
print("\n")


# ==========================================
# Q6 – Recursion and Its Limits
# ==========================================

from functools import lru_cache

calls = 0

def ways_naive(n):
    """Ways to climb n temple steps taking 1 or 2 steps at a time."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    # TODO 1: Write the same base case and recursive case as ways_naive, calling ways_memo
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

print("--- Q6 Results ---")
calls = 0; print("naive:", ways_naive(25), "calls =", calls)
calls = 0; print("memo :", ways_memo(25), "calls =", calls)
