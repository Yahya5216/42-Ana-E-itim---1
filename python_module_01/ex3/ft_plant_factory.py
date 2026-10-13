class Plant:
    def __init__(self, name: str, height: float, current_age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = current_age

    def show(self) -> None:
        plant_name = self.name.capitalize()
        print(f"{plant_name}: {self.height}cm, {self.current_age} days old")

    def grow(self) -> None:
        self.height += 0.5

    def age(self) -> None:
        self.current_age += 1


def ft_plant_factory() -> None:
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
