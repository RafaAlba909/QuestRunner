
class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item} añadido al inventario.")

    def show(self):
        if self.items:
            print("Tu inventario contiene:")
            for item in self.items:
                print(f" - {item}")
        else:
            print("Tu inventario está vacío.")
