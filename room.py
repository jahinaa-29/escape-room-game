from visuals import show_img

class Room:
    def __init__(self, name, description, img=None, dark=False):
        self.name = name
        self.description = description
        self.dark = dark
        self.img = img
        self.connections = {} # i.e. which room it leads to
        self.items = []

    def connect(self, direction, room):
        self.connections[direction] = room

    def describe(self, has_light=True):
        print(f"\n⊹₊˚︵‿₊. {self.name} ☆.₊‿︵˚₊⊹")

        if self.dark and not has_light:
            print("\nThe room is pitch black. You can't see anything.")
        else:
            if self.img:
                show_img(self.img)
            print(f"\n{self.description}")

        print("\nExits:")
        for direction in self.connections:
            print("-", direction)
            