import json
from validator import validate_attendee

with open("data/attendees.json", "r", encoding="utf-8") as f:
    attendees = json.load(f)

valid_count = 0
invalid_count = 0

for attendee in attendees:
    errors = validate_attendee(attendee)
    if errors:
        invalid_count += 1
        print(f"[INVALID] {attendee.get('name', 'Unknown')}: {errors}")
    else:
        valid_count += 1
        print(f"[VALID] {attendee['name']}")

print("\nSummary")
print(f"Valid attendees: {valid_count}")
print(f"Invalid attendees: {invalid_count}")