from room import Room
from player import Player
from item import Item
from visuals import show_img

class Game:
    def __init__(self):
        self.drawer_open = False
        self.create_world()
        

    def create_world(self): 

        # -----creating the rooms-----

        lab = Room(
            "Main Laboratory",
            "It's dark. The old laboratory is filled with scattered abandoned equipment.",
            "lab"
        )

        print("LAB IMAGE: ", lab.img)

        office = Room(
            "Office",
            "A cramped dimly lit office with a desk which has a locked drawer.",
            "office"
        )

        storage = Room(
            "Storage Room",
            "Shelves line the peeling walls. Something is hidden here.",
            "storage"
        )

        control = Room(
            "Control Room",
            "A massive control panel covers the walls. A security terminal flashes beside the exit door.",
            "control"
        )

        # -------create the items---------

        key = Item(
            "Brass Key",
            "A small rusted brass key you found in your pocket upon waking up."
        )

        flashlight = Item(
            "Flashlight",
            "An old black worn flashlight. It still works.",
            "flashlight"
        )

        battery = Item(
            "Battery",
            "A heavy industrial battery used to power a control terminal.",
            "battery"
        )

        badge = Item(
            "Security Badge",
            "An unknown employee security badge with high level clearance.",
            "badge"
        )

        note = Item(
            "Security Code Note",
            "A sticky note that reads: 'Emergency Override Code: 1017'.",    
            "note"
        )       


        # -------connect all the rooms to each other------

        lab.connect("office", office) 
        lab.connect("storage", storage) 

        office.connect("lab", lab)
        storage.connect("lab", lab)

        office.connect("control", control)
        control.connect("office", office)

        # Spawns player in the lab with a key
        self.player = Player(lab)
        self.key = key
        self.player.inventory.append(key)

        # Place all the items in their respective rooms
        self.badge = badge
        self.note = note
        lab.items.append(flashlight)
        storage.items.append(battery)

    def search_room(self):
        room = self.player.current_room

        print("\nYou searched the room...")

        if room.name == "Office" and not self.drawer_open:
            print("Hmm... You notice a locked desk drawer... (Hint... Check commands again with 'help')")
            return

        if not room.items:
            print("Nothing useful was found.")
            return

        print("\nYou found:")

        for item in room.items:
            print("\nYou found:")
            print(item.name)

            if item.img:
                show_img(item.img)

            print(item.description)

            self.player.inventory.append(item)

        room.items.clear()

    def open_drawer(self):
        if self.player.current_room.name != "Office":
            print("There is no locked drawer here.")
            return

        if self.drawer_open:
            print("The drawer is already open.")
            return

        has_key = False

        for item in self.player.inventory:
            if item.name == "Brass Key":
                has_key = True

        if has_key:
            print("\nYou insert the Brass Key into the drawer and turn.")
            print("Click.")

            print("\nInside, you find:")

        for item in [self.badge, self.note]:
            print("\n" + item.name)

            if item.img:
                show_img(item.img)

            print(item.description)

            self.player.inventory.append(item)

        else:
            print("The drawer is locked.")

    def escape(self):

        if self.player.current_room.name != "Control Room":
            print("There is no exit here. Hint: Try 'escape'")
            return

        has_badge = False

        for item in self.player.inventory:
            if item.name == "Security Badge":
                has_badge = True

        if has_badge:
            print("""
            You approach the security terminal.

            You swipe the Security Badge.

            ...

            ACCESS GRANTED.

            The emergency exit door unlocks.

            You step outside into the cold night air.

            =========================
                YOU ESCAPED!
            =========================
            """)

            show_img("exit")

            quit()

        else:
            print("The terminal flashes red.")
            print("Security clearance required.")
        

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

            if command.startswith("m "):
                direction = command.split(" ")[1]
                self.player.move(direction)

            elif command == "e":
                self.player.current_room.describe()


            elif command == "inv":
                self.player.show_inventory()

            elif command == "s":
                self.search_room()

            elif command.startswith("i "):
                item_name = command[2:]
                self.player.inspect_item(item_name)

            elif command == "open drawer":
                self.open_drawer()

            elif command == "escape":
                self.escape()

            elif command == "help":
                print("""
                                Commands:
                ------------------------------------------
                m <insert room name> - move
                e - explore the room
                s - search the room
                i <insert item name> - inspect the item
                inv - check inventory

                Special commands: 
                -------------------
                In Office, use 'open drawer'
                In Control Room, use "escape"


                help
                quit

                """)

            elif command == "quit":
                            print("Game Over.")
                            break

            else:
                print("Command not found. Type 'help' to view available commands.")