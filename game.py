from room import Room
from player import Player

class Game:
    def __init__(self):
        self.create_world()

    def create_world(self): # creating the rooms
        lab = Room(
            "Main Laboratory",
            "It's dark. The old laboratory is filled with scattered abandoned equipment."
        )

        office = Room(
            "Office",
            "A cramped dimly lit office with a desk which has a locked drawer."
        )

        storage = Room(
            "Storage Room",
            "Shelves line the peeling walls. Something is hidden here."
        )

        # connect all the rooms to each other

        lab.connect("office", office) 
        lab.connect("storage", storage) 

        office.connect("lab", lab)
        storage.connect("lab", lab)

        self.player = Player(lab) # Spawns player in the lab

        # start the game

    def start(self):
        print("================================================================")
        print("= = = = = = = = = = = = ESCAPE THE LAB = = = = = = = = = = = = =")
        print("================================================================")

        print("\nYou wake up in an abandoned lab.")

        self.player.current_room.describe()
        self.game_loop()

    def game_loop(self):
        while True:
            command = input("\n> ").lower()

            if command.startswith("move"):
                direction = command.split(" ")[1]
                self.player.move(direction)

            elif command == "explore":
                self.player.current_room.describe()

            elif command == "quit":
                print("Game Over.")
                break

            else:
                print("Invalid command.")