class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {} # i.e. which room it leads to

    def connect(self, direction, room):
        self.connections[direction] = room

    def describe(self):
        print(f"\n⊹₊˚︵‿₊. {self.name} ☆.₊‿︵˚₊⊹")
        print(f"\n{self.description}")

        print("\nExits:")
        for direction in self.connections:
            print("-", direction)

            