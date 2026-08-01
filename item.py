from visuals import show_img

class Item:
    def __init__(self, name, description, img=None):
        self.name = name
        self.description = description
        self.img = img

    def inspect(self):
        print(f"\n{self.name}")

        if self.img:
            show_img(self.img)

        print(self.description)