from room import Room
from player import Player
from item import Item
from visuals import show_img

class Game:
    def __init__(self):
        self.create_world()

    def create_world(self): 

        # -----creating the rooms-----

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

        # -------create the items---------

        key = Item(
            "Brass Key",
            "A small rusted brass key you found in your pocket upon waking up."
        )

        flashlight = Item(
            "Flashlight",
            "An old black worn flashlight. It still works."
        )

        battery = Item(
            "Battery",
            "A heavy industrial battery used to power a control terminal."
        )

        badge = Item(
            "Security Badge",
            "An unknown employee security badge with high level clearance."
        )

        note = Item(
            "Security Code Note",
            "A sticky note that reads: 'Emergency Override Code: 1017'."    
        )       


        # -------connect all the rooms to each other------

        lab.connect("office", office) 
        lab.connect("storage", storage) 

        office.connect("lab", lab)
        storage.connect("lab", lab)

        # Spawns player in the lab with a key
        self.player = Player(lab)
        self.key = key
        self.player.inventory.append(key)

        # Place all the items in their respective rooms
        lab.items.append("Flashlight")
        office.items.append("Security Badge")
        office.items.append("Security Code Note")
        storage.items.append("Battery")

    def search_room(self):
        room = self.player.current_room

        print("\n You searched the room...")

        if not room.items:
            print("Nothing useful was found.")
            return

        print("\nYou found:")

        for item in room.items:
            print("-", item)
            self.player.inventory.append(item)

        # removes duplicate items in the room that have already been found
        room.items.clear() 
        


    # ----start the game----

    def start(self):
        print(r"""
        ------------------------------------------------------------

            ░█▀▀░█▀▀░█▀▀░█▀█░█▀█░█▀▀░░░▀█▀░█░█░█▀▀░░░█░░░█▀█░█▀▄░░
            ░█▀▀░▀▀█░█░░░█▀█░█▀▀░█▀▀░░░░█░░█▀█░█▀▀░░░█░░░█▀█░█▀▄░░
            ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░░░░▀░░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀▀░░░


            >>>> COMMANDS <<<<<
                m <insert room name> - move
                e - explore the room
                s - search the room
                i <insert item name> - inspect the item
                inv - check inventory
            
                help
                quit

        ------------------------------------------------------------

        """)

        print("\nYou wake up dazed in an abandoned lab. You don't remember how you got here.")
        print("\nYou feel something in your pockets. You check to find a Brass Key.")
        show_img("key")
        print("You found a Brass Key.")

        self.player.current_room.describe()
        self.game_loop()

    def game_loop(self):
        while True:
            command = input("\n> ").lower()

            if command.startswith("m"):
                direction = command.split(" ")[1]
                self.player.move(direction)

            elif command == "e":
                self.player.current_room.describe()


            elif command == "i":
                self.player.show_inventory()

            elif command == "s":
                self.search_room()

            elif command == "help":
                print("""
                                Commands:
                ------------------------------------------
                m <insert room name> - move
                e - explore the room
                s - search the room
                i <insert item name> - inspect the item
                inv - check inventory

                help
                quit

                """)

            elif command == "quit":
                            print("Game Over.")
                            break

            else:
                print("Command not found. Type 'help' to view available commands.")