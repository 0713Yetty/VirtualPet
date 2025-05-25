# storage.py

import os

# Save pet status to a text file in readable format
def save_pet(pet):
    filename = f"{pet.name}.txt"
    with open(filename, "w") as f:
        f.write(f"Name: {pet.name}\n")
        f.write(f"Species: {pet.species}\n")
        f.write(f"Personality: {pet.personality}\n")
        f.write(f"Hunger: {pet.hunger}\n")
        f.write(f"Happiness: {pet.happiness}\n")
        f.write(f"Cleanliness: {pet.cleanliness}\n")
        f.write(f"Energy: {pet.energy}\n")
        f.write(f"HappinessHistory: {','.join(map(str, pet.happiness_history))}\n")
    print("💾 Pet saved in readable format!")

# Load pet status from a text file in readable format
def load_pet(name):
    filename = f"{name}.txt"
    try:
        with open(filename, "r") as f:
            lines = f.read().splitlines()

        data = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()

        from Pet import Pet
        pet = Pet(name=data["Name"], species=data["Species"], personality=data.get("Personality", "playful"))
        pet.hunger = int(data.get("Hunger", 5))
        pet.happiness = int(data.get("Happiness", 7))
        pet.cleanliness = int(data.get("Cleanliness", 6))
        pet.energy = int(data.get("Energy", 6))

        if "HappinessHistory" in data:
            pet.happiness_history = list(map(int, data["HappinessHistory"].split(",")))
        else:
            pet.happiness_history = [pet.happiness]

        print("📂 Pet loaded successfully!")
        return pet

    except FileNotFoundError:
        print("📁 No previous pet data found. Starting a new adventure!")
        return None
    except Exception as e:
        print(f"⚠️ Error loading pet data: {e}")
        return None

# List all available pets by scanning current directory for .txt files
def list_pets():
    return [f[:-4] for f in os.listdir() if f.endswith(".txt") and f not in ("pet_log.txt", "pet_list.txt","pet_data.txt")]

# Add a pet name to a registry list (optional)
def register_pet(name):
    try:
        with open("pet_list.txt", "a") as f:
            f.write(name + "\n")
    except:
        pass
