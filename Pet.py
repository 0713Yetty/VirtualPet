import random
from emotions import EMOTIONS

class Pet:
    def __init__(self, name, species="pet", personality="playful"):
        # Initialize pet attributes
        self.name = name
        self.species = species
        self.personality = personality
        self.hunger = 5
        self.happiness = 7
        self.cleanliness = 6
        self.energy = 6
        self.happiness_history = [self.happiness]

    def _say(self, mood_key):
        # Get emotion-based expression
        expressions = EMOTIONS.get(self.species, EMOTIONS["default"])
        lines = expressions.get(mood_key, expressions["neutral"])
        print(random.choice(lines))

    def feed(self):
        # Reduce hunger, increase energy
        if self.hunger <= 0:
            print(f"{self.name} is already full! 🍗")
            self._say("full")
        else:
            self.hunger = max(self.hunger - 2, 0)
            self.energy = min(self.energy + 1, 10)
            print(f"{self.name} eats joyfully! ε==3 Bone time!")
            self._say("fed")

    def play(self):
        # Boost happiness, reduce cleanliness and energy
        if self.energy < 2:
            print(f"{self.name} is too tired to play... 😴")
            self._say("tired")
        elif self.hunger > 8:
            print(f"{self.name} is too hungry to play... 😖")
            self._say("hungry")
        else:
            self.happiness = min(self.happiness + 2, 10)
            self.energy = max(self.energy - 1, 0)
            self.cleanliness = max(self.cleanliness - 1, 0)
            print(f"{self.name} rolls and jumps with joy! ✧⁺⸜(˙▾˙)⸝⁺✧")
            self._say("playful")

    def clean(self):
        # Clean the pet, reduce happiness slightly
        if self.cleanliness >= 10:
            print(f"{self.name} is already super clean ✨")
            self._say("sparkly")
        else:
            self.cleanliness = 10
            self.happiness = max(self.happiness - 1, 0)
            print(f"{self.name} is clean and shiny now... but maybe a little grumpy 🛁")
            self._say("bathed")

    def rest(self):
        # Let pet rest to regain energy, increases hunger
        if self.energy >= 10:
            print(f"{self.name} is already full of energy! ⚡")
            self._say("hyper")
        else:
            self.energy = min(self.energy + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} curls up and naps... (｡•ᴗ-)_ 💭")
            self._say("sleepy")

    def status(self):
        # Display pet status in a framed format (top and bottom borders only)
        bar = lambda val: "█" * val + " " * (10 - val)

        lines = [
            f" Name        : {self.name}",
            f" Species     : {self.species}",
            f" Hunger      : {bar(self.hunger)}   ({self.hunger:>2}/10)",
            f" Happiness   : {bar(self.happiness)}   ({self.happiness:>2}/10)",
            f" Cleanliness : {bar(self.cleanliness)}   ({self.cleanliness:>2}/10)",
            f" Energy      : {bar(self.energy)}   ({self.energy:>2}/10)",
            f" Mood        : {self.get_mood()}",
        ]

        width = max(len(l) for l in lines) + 4  # padding for frame
        border = "─" * width
        print(f"\n{border}")
        title = " PET STATUS "
        print(title.center(width))
        print(border)
        for l in lines:
            print(l)
        print(f"{border}\n")

    def get_mood(self):
        # Return mood description based on current state
        if self.happiness >= 8 and self.energy >= 6:
            return "(｡♥‿♥｡) Feeling awesome!"
        elif self.hunger >= 8:
            return "(╥﹏╥) Hungry and sad..."
        elif self.cleanliness <= 3:
            return "(｡•́︿•̀｡) I feel dirty..."
        elif self.energy <= 2:
            return "(-_-) Sleepy..."
        else:
            return "(・_・;) Doing okay"

    def update_history(self):
        # Track happiness over time
        self.happiness_history.append(self.happiness)

    def show_growth(self):
        # Show happiness growth as a bar graph
        print("\n📈 Happiness History:")
        for i, val in enumerate(self.happiness_history, 1):
            print(f"Day {i}: {'▉' * val} ({val}/10)")

    def quiz(self):
        # Simple quiz interaction with reward or penalty
        questions = [
            ("What color is the sky?", "blue"),
            ("What do cats say?", "meow"),
            ("What's 2 + 2?", "4")
        ]
        q, a = random.choice(questions)
        print(f"🧠 {self.name}'s quiz time! Answer this:")
        answer = input(f"{q} ").strip().lower()
        if answer == a:
            print("(⁎⁍̴̛ᴗ⁍̴̛⁎) Yay! Correct!")
            self.happiness = min(self.happiness + 1, 10)
        else:
            print("(｡•́︿•̀｡) Oops, that's not right...")
            self.happiness = max(self.happiness - 1, 0)
