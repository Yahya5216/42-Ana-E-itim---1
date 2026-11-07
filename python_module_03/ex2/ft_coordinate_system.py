import math


def get_value() -> tuple[float, float, float]:
    while True:
        data = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x_str, y_str, z_str = data.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        valid = True
        for part in (x_str, y_str, z_str):
            part = part.strip()
            try:
                coords.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                valid = False
                break
        if valid:
            return (coords[0], coords[1], coords[2])


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    return math.sqrt((p2[0] - p1[0]) ** 2
                     + (p2[1] - p1[1]) ** 2
                     + (p2[2] - p1[2]) ** 2)


def get_player_pos() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    first = get_value()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    center = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(distance(center, first), 4)}")

    print("\nGet a second set of coordinates")
    second = get_value()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance(first, second), 4)}")


if __name__ == "__main__":
    get_player_pos()
