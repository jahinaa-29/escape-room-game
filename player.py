class Player:
    def __init__(self, start_room):
        self.current_room = start_room

    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            self.current_room.describe()
        else:
            print("You cannot go that way.")
        