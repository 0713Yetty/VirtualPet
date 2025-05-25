import time
from pet_log import log_action, log_status
from Pet import Pet
from storage import save_pet, load_pet, list_pets, register_pet

# Print the framed menu
def display_menu():
    lines = [
        "What would you like to do today with your fluffy friend?",
        "1. Feed 🍗",
        "2. Play 🎾",
        "3. Clean 🛁",
        "4. Rest 💤",
        "5. Check status 📊",
        "6. Show happiness growth chart 📈",
        "7. Quiz time 🧠",
        "8. Save and quit 💾",
    ]

    width = max(len(l) for l in lines) + 4  # padding
    bar = "─" * width

    print(f"\n{bar}")
    print("  MENU ".center(width))
    print(bar)
    for l in lines:
        print("  " + l)
    print(bar)


# Greeting message
print("\nʕ•ᴥ•ʔ Welcome to Your Virtual Pet Adventure! ʕ•ᴥ•ʔ")
print("Let's have some fun with your adorable little buddy!\n")
time.sleep(1)

# Ask the user whether to load or create a new pet
print("🐾 Do you want to load your previous pet or create a new one?")
print("1. Load previous pet 📂")
print("2. Create a new pet 🐣")
choice = input("Enter 1 or 2: ").strip()
while choice not in ("1", "2"):
    choice = input("Please enter 1 or 2: ").strip()

pet = None
if choice == "1":
    existing_pets = list_pets()
    if not existing_pets:
        print("⚠️  No saved pets found, creating a new one instead.")
        time.sleep(1)
    else:
        print("📜 Available pets:")
        for i, name in enumerate(existing_pets, 1):
            print(f"{i}. {name}")
        index = input("Choose a pet number: ").strip()
        while not index.isdigit() or not 1 <= int(index) <= len(existing_pets):
            index = input("Please enter a valid number: ").strip()
        pet_name = existing_pets[int(index) - 1]
        pet = load_pet(pet_name)
        time.sleep(1)

if not pet:
    name = input("🌟 Name your pet: > ").strip()
    while not name:
        name = input("Name can't be empty! Try again: > ").strip()

    species = input("🐾 Species (dog/cat/bird/etc): > ").strip()
    while not species:
        species = input("Species can't be empty! Try again: > ").strip()

    pet = Pet(name=name, species=species)
    register_pet(name)
    log_action("Created new pet", pet.name)
    time.sleep(1)

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-8): > ").strip()

    if not choice.isdigit() or not 1 <= int(choice) <= 8:
        print("⚠️  Please choose a number between 1 and 8.")
        time.sleep(1)
        continue

    if choice == "1":
        pet.feed()
        pet.update_history()
        log_action("Fed", pet.name)
    elif choice == "2":
        pet.play()
        pet.update_history()
        log_action("Played", pet.name)
    elif choice == "3":
        pet.clean()
        pet.update_history()
        log_action("Cleaned", pet.name)
    elif choice == "4":
        pet.rest()
        pet.update_history()
        log_action("Rested", pet.name)
    elif choice == "5":
        pet.status()
        log_status(pet)
    elif choice == "6":
        pet.show_growth()
    elif choice == "7":
        pet.quiz()
        pet.update_history()
        log_action("Quiz", pet.name)
    elif choice == "8":
        confirm = input("\n💾 Save before quitting? (y/n): ").strip().lower()
        while confirm not in ("y", "n"):
            confirm = input("Please enter 'y' or 'n': ").strip().lower()
        if confirm == "y":
            save_pet(pet)
            print("✅ Pet saved successfully!")
        print(f"\n(｡•́︿•̀｡) {pet.name} waves a tiny paw… Come back soon!")
        time.sleep(1)
        break

    time.sleep(1)
    cont = input("\n🌼 Continue playing? (y/n): ").strip().lower()
    while cont not in ("y", "n"):
        cont = input("Please enter 'y' or 'n': ").strip().lower()
    if cont == "n":
        confirm = input("\n💾 Save before exiting? (y/n): ").strip().lower()
        while confirm not in ("y", "n"):
            confirm = input("Please enter 'y' or 'n': ").strip().lower()
        if confirm == "y":
            save_pet(pet)
            print("✅ Pet saved successfully!")
        print(f"\n(｡•́︿•̀｡) {pet.name} snuggles into bed… See you next time!")
        time.sleep(1)
        break
