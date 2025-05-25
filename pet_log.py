import datetime

# Log a simple action with timestamp and pet name
def log_action(action, pet_name, filename="pet_log.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {pet_name} - {action}\n"
    with open(filename, "a") as f:
        f.write(entry)

# Log full pet status to file with timestamp
def log_status(pet, filename="pet_log.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = (
        f"\n[{timestamp}] {pet.name}'s current status:\n"
        f"  Hunger      : {pet.hunger}/10\n"
        f"  Happiness   : {pet.happiness}/10\n"
        f"  Cleanliness : {pet.cleanliness}/10\n"
        f"  Energy      : {pet.energy}/10\n"
        f"  Mood        : {pet.get_mood()}\n"
        "---------------------------------------------\n"
    )
    with open(filename, "a") as f:
        f.write(status)
