class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0.0
        self.current_age = 0

    def show(self) -> None:
        plant_name = self.name.capitalize()
        print(f"{plant_name}: {self.height}cm, {self.current_age} days old")

    def grow(self) -> None:
        self.height += 0.5

    def age(self) -> None:
        self.current_age += 1


def ft_plant_growth() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.current_age = 30

    initial_height = rose.height

    print("=== Garden Plant Registry ===")
    rose.show()
    for day in range(1, 8):
        rose.age()
        rose.grow()
        print(f"=== Day {day} ===")
        rose.show()
    total_growth = rose.height - initial_height
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
