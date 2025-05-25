# Virtual Pet Game

A simple command-line based virtual pet game written in Python. You can feed, play, clean, rest, check status, and answer quiz questions to interact with your pet.

---

## Features

- Feed: decreases hunger, increases energy  
- Play: increases happiness, reduces cleanliness and energy  
- Clean: restores cleanliness, slightly reduces happiness  
- Rest: increases energy and hunger  
- Status: shows current status with mood  
- Quiz: small trivia for happiness bonus  
- Save and load pets (each pet saved as a separate `.txt` file)  
- Logs actions and status to `pet_log.txt`

---

## How to Run

1. Make sure Python 3 is installed  
2. Open terminal and navigate to the project folder  
3. Run the program:
   ```
   python3 main.py
   ```

---

## File Structure

```
VirtualPet/
│
├── main.py         # Main loop and menu
├── pet.py          # Pet class and behaviors
├── emotions.py     # Mood expressions
├── storage.py      # Save/load pet data
├── pet_log.py      # Logs actions to file
├── *.txt           # Individual pet data files
├── pet_log.txt     # Interaction log
└── README.md       # Project description
```
