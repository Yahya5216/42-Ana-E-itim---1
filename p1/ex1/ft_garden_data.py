class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0
        self.age = 0

    def show(self) -> None:
        plant_name = self.name.capitalize()
        print(f"{plant_name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.age = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age = 120

    plants = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_garden_data()
