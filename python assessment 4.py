import os
import tempfile

class InvalidRecord(Exception):
    """Raised when a line of the attendance file is not in the expected format."""

def parse_line(line):
    """'192311001,2026-10-08,P' -> ('192311001', '2026-10-08', 'P')"""
    parts = line.strip().split(",")
    if len(parts) != 3 or parts[2] not in ('P', 'A'):
        if len(parts) != 3:
            raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
        else:
            raise InvalidRecord(f"invalid status '{parts[2]}'")
    return tuple(parts)

def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    reg, date, status = parse_line(line)
                    if status == 'P':
                        present += 1
                    elif status == 'A':
                        absent += 1
                except InvalidRecord as e:
                    errors.append((line_num, str(e)))
                except Exception as e:
                    errors.append((line_num, f"unexpected error: {str(e)}"))
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    return present, absent, errors

# Testing the implementation
data = ("192311001,2026-10-08,P\n192311002,2026-10-08,A\n"
"192311003,2026-10-08\n192311004,2026-10-08,L\n")

with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
    tmp.write(data)
    temp_name = tmp.name

print(summarise(temp_name))
os.remove(temp_name)
