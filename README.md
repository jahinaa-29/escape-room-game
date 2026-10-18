# Escape the Lab

## Description

A text-based escape room adventure game built in Python for CS3003 Programming Languages. The project demonstrates object-oriented programming concepts through interactive gameplay, object management, and modular program design.

## Project Overview

The player wakes up in an abandoned laboratory with no memory of how they arrived. Using exploration, item collection, and interactions with the environment, the player must navigate through different rooms, unlock restricted areas, and escape the lab.

The game is implemented using Python and focuses on applying object-oriented programming principles, including encapsulation, object interaction, and modular class design.

## Features

- Text-based adventure gameplay
- Multiple connected rooms to explore
- ASCII art visuals loaded from external files
- Item collection and inventory management
- Item inspection system
- Locked drawer interaction using inventory items
- Escape sequence with a final objective

## Gameplay

The player begins in the Main Laboratory with a Brass Key.

<details>
<summary>Example gameplay flow:</summary>


1. Explore the Main Laboratory
2. Search rooms to discover useful items
3. Collect the Flashlight and Battery
4. Travel to the Office
5. Unlock the desk drawer using the Brass Key
6. Obtain the Security Badge
7. Access the Control Room
8. Escape the laboratory
</details>

## Commands

| Command | Description |
|---|---|
| `m <room>` | Move to another room |
| `e` | Explore the current room |
| `s` | Search the current room |
| `inv` | View inventory |
| `i <item>` | Inspect an item |
| `open drawer` | Unlock the office drawer |
| `escape` | Attempt to escape from the Control Room |
| `help` | Display available commands |
| `quit` | Exit the game |

## How to Run
In terminal, enter the following commands:

`% git clone [<repo-u>](https://github.com/jahinaa-29/escape-room-game.git)`  
`% cd escape-the-lab`  
`% python3 main.py`

## Future Improvements


## Project Structure
```
escape-sequence/  
│  
├── main.py # Program entry point  
├── game.py # Main game logic and interactions  
├── room.py # Room class definition  
├── player.py # Player movement and inventory system  
├── item.py # Item class definition  
├── visuals.py # ASCII art loading functionality  
│  
├── assets/ # dot art files  
│ ├── lab.txt  
│ ├── office.txt  
│ ├── storage.txt  
│ ├── control.txt  
│ ├── key.txt  
│ └── note.txt  
│ └── battery.txt  
│ └── exit.txt  
│  
├── README.md  
└── requirements.txt  
```
---

Built for CS3003 Programming Languages, Summer 2026

