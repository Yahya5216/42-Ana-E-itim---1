
class Plant:
    class PlantStats:
        def __init__(self, is_tree: bool = False) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._is_tree = is_tree
            self._shade_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def increment_shade(self) -> None:
            if self._is_tree:
                self._shade_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )
            if self._is_tree:
                print(f"{self._shade_count} shade")

    def __init__(
        self,
        name: str,
        height: float,
        current_age: int,
        is_tree: bool = False
    ) -> None:
        self._name = name
        self._height = height
        self._current_age = current_age
        self._stats = self.PlantStats(is_tree=is_tree)

    def get_name(self) -> str:
        return self._name

    def show(self) -> None:
        self._stats.increment_show()
        plant_name = self._name
        if self._name != "Unknown plant":
            plant_name = self._name.capitalize()
        print(
            f"{plant_name}: {self._height}cm, "
            f"{self._current_age} days old"
        )

    def grow(self, amount: float) -> None:
        self._stats.increment_grow()
        self._height += amount

    def age(self, days: int) -> None:
        self._stats.increment_age()
        self._current_age += days

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        current_age: int,
        color: str
    ) -> None:
        super().__init__(name, height, current_age)
        self._color = color
        self._is_bloomed = False

    def bloom(self) -> None:
        self._is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        current_age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, current_age, is_tree=True)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.increment_shade()
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        current_age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, current_age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        current_age: int,
        color: str
    ) -> None:
        super().__init__(name, height, current_age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    name_str = plant.get_name()
    if name_str != "Unknown plant":
        name_str = name_str.capitalize()
    print(f"[statistics for {name_str}]")
    plant.display_stats()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year?-> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year?-> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
