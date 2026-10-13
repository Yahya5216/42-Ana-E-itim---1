class Plant:
    def __init__(self, name: str, height: float, current_age: int) -> None:
        self._name = name
        self._height = height
        self._current_age = current_age
        print(f"Plant created: {self._name}: {self._height}cm, {self._current_age} days old")
  
    def show(self) -> None:
        plant_name = self._name.capitalize()
        print(f"{plant_name}: {self._height}cm, {self._current_age} days old")

    def grow(self, amount) -> None:
        self._height += amount

    def age(self, days) -> None:
        self._current_age += days


class Flower(Plant):
    def __init__(self, name, height, current_age, color):
        super().__init__(name, height, current_age)
        self._is_bloomed = False
        self._color = color
    
    def bloom(self) -> int:
        print("[asking the rose to bloom]")
        self._is_bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._is_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

class Tree(Plant):
    def __init__(self, name, height, current_age, trunk_diameter):
        super().__init__(name, height, current_age)
        self._trunk_diameter = trunk_diameter

    def  produce_shade(self):
        print("[asking the oak to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")

class Vegetable(Plant):
    def __init__(self, name, height, current_age, harvest_season):
        super().__init__(name, height, current_age)
        self._nutritional_value = 0
        self._harvest_season = harvest_season

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days):
        super().age(days)
        self._nutritional_value += days
    

def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()
    

if __name__ == "__main__":
    ft_plant_types()