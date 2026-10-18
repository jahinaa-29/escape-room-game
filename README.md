# Escape the Lab

## Description

A text-based escape room adventure game built in Python for CS3003 Programming Languages. The project demonstrates object-oriented programming concepts through interactive gameplay, object management, and modular program design.

## Project Overview

The player wakes up in an abandoned laboratory with no memory of how they arrived. By exploring, collecting items, and using them on the environment, the player must navigate the lab, unlock restricted areas, restore power to the control panel, and **escape the lab**.

The game focuses on applying object-oriented programming principles, including encapsulation, object interaction, and modular class design.

## Features

- Text-based adventure gameplay with multiple connected rooms
- ASCII art visuals loaded from external files
- Item collection, inspection, and inventory management
- Item usage system (u): toggle the flashlight, power the control panel with the battery
- Dark rooms that cannot be seen or searched without a lit flashlight
- Locked drawer that requires the Brass Key
- Multi-step puzzle chain: flashlight → battery → key → badge → code → escape
- Control terminal with power check, badge check, and code entry

## Example Gameplay Walkthrough

https://github.com/user-attachments/assets/cd7a824b-63f3-422c-aea5-962c7966fd42

<details>
<summary>Full Walkthrough Steps</summary>

1. Start in the Main Laboratory. Re-read the room description and check your inventory, which holds only the Brass Key. Inspect the key to learn more about it.
2. Head into the Storage room without a light source. It's pitch black, and searching fails because it's too dark to see anything.
3. Go back to the lab and search it to find the Flashlight. Your inventory now has the key and the flashlight.
4. Return to Storage. The flashlight isn't on yet, so it's still dark. Switch the flashlight on and the room is described again, now fully visible.
5. Search Storage to find the Battery.
6. Try switching the flashlight off and on. When it's off the room goes dark again, and turning it back on restores your view.
7. Travel back through the lab to the Office. Searching hints at a locked desk drawer.
8. Use the Brass Key to unlock the drawer and take the Security Badge and a Security Code Note. Inspect the note to read the four-digit code.
9. Go to the Control Room and try to escape. The terminal is dead and needs a power source.
10. Insert the Battery. The panel powers on and the battery is used up.
11. Try to escape again. The badge check passes and you're asked for the access code.
12. Enter the wrong code and you get ACCESS DENIED. Re-read the note to check the code, try again with the right one, and you escape the lab.

</details>

## Commands

| Command | Description |
|---|---|
| `m <room>` | Move to another room |
| `e` | Explore the current room |
| `s` | Search the current room |
| `inv` | View inventory |
| `i <item>` | Inspect an item |
| `u <item>` | Use an item (e.g. u flashlight, u battery) |
| `open drawer` | Unlock the office drawer |
| `escape` | Attempt to escape from the Control Room |
| `help` | Display available commands |
| `quit` | Exit the game |

## How to Run
Requires Python 3. In a terminal, run:

`% git clone [<repo-u>](https://github.com/jahinaa-29/escape-room-game.git)`  
`% cd escape-the-lab`  
`% python3 main.py`

## OOP Principles Demonstrated

| Class | Principle Demonstrated |
|---|---|
| `Room` | Encapsulation of room state (name, description, darkness, items); connections between rooms form a graph |
| `Player` | Inventory management and a single source of truth for light state (has_light()) |
| `Item` | Simple data object with an optional ASCII art image |
| `Game` | 	Orchestration of the game loop and global state (drawer unlocked, panel powered) |


## Project Structure
```
escape-sequence/  
│  
├── main.py               # Program entry point  
├── game.py               # Main game logic and interactions  
├── room.py               # Room class definition  
├── player.py             # Player movement and inventory system  
├── item.py               # Item class definition  
├── visuals.py            # ASCII art loading functionality  
│  
├── assets/               # ASCII art files  
│ ├── lab.txt  
│ ├── office.txt  
│ ├── storage.txt  
│ ├── control.txt  
│ ├── key.txt
│ ├── flashlight.txt
│ ├── battery.txt
│ ├── badge.txt
│ └── note.txt  
│ └── exit.txt  
│  
├── README.md  
└── requirements.txt  
```

## Future Improvements
- Save and load game state
- A move counter or timer with a score at the end
- A hint command
- More rooms and a second ending

---
Built by Aisha Arina Jahin for CS3003 Programming Languages, University of Cincinnati, Summer 2026

