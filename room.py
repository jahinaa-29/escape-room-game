from visuals import show_img

class Room:
    def __init__(self, name, description, img=None):
        self.name = name
        self.description = description
        self.img = img
        self.connections = {} # i.e. which room it leads to
        self.items = []

    def connect(self, direction, room):
        self.connections[direction] = room

    def describe(self):
        print(f"\n⊹₊˚︵‿₊. {self.name} ☆.₊‿︵˚₊⊹")

        if self.img:
            show_img(self.img)

        print(f"\n{self.description}")

        print("\nExits:")
        for direction in self.connections:
            print("-", direction)
            