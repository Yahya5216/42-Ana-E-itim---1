class Plant:
    def __init__(self, name: str, height: float, current_age: int) -> None:
        self._name = name
        self._name = self._name.capitalize()
        self._height = 0.0
        self._current_age = 0

        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")

        if current_age >= 0:
            self._current_age = current_age
        else:
            print(f"{self._name}: Error, age can't be negative")

        print(
            f"Plant created: {self._name}: "
            f"{self._height}cm, {self._current_age} days old"
        )

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {round(self._height)}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, current_age: int) -> None:
        if current_age >= 0:
            self._current_age = current_age
            print(f"Age updated: {self._current_age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._current_age
    
    def show(self) -> None:
        print(f"Current state: {self._name}: {self._height}cm, {self._current_age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("")
    rose.set_height(25.0)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    rose.set_age(-6)
    print("")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
