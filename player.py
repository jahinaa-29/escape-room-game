class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []                 # collect items as you go

    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            self.current_room.describe()
        else:
            print("You cannot go that way.")

    def show_inventory(self):
        if not self.inventory:
            print("\nYour inventory is empty.")

        else:
            print("\nYour Inventory:")
            for item in self.inventory:
                print("-", item.name)

    def inspect_item(self, name):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                item.inspect()
                return

        print("Item not found in inventory.")

    def use_item(self, name):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item

        print("Item not found in inventory.")
        return None