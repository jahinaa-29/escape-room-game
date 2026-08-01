import os

def show_img(filename):
    # show dot art image from assets folder.

    filepath = os.path.join("assets", f"{filename}.txt")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print(f"[Image '{filename}' not found.]")