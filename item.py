class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def inspect(self):
        print(f"\n{self.name}")
        print(self.description)

    