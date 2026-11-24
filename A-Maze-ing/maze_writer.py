"""Labirenti hexadecimal duvar formatinda dosyaya yazma islemleri.
(0,0) → (1,0) : Doğu  → E
(1,0) → (1,1) : Güney → S
(1,1) → (0,1) : Batı  → W
Sonuç:
ESW
"""


def path_to_directions(path: list[tuple[int, int]]) -> str:
    """Convert a coordinate path to N, E, S, W directions."""
    direction_map = {
        (0, -1): "N",
        (1, 0): "E",
        (0, 1): "S",
        (-1, 0): "W",
    }

    directions: list[str] = []

    # 1 çıkarmamızın sebebi her hücreyi bir sonrakiyle karşılaştırıyoruz
    for index in range(len(path) - 1):
        x, y = path[index]
        next_x, next_y = path[index + 1]

        movement = (next_x - x, next_y - y)

        if movement not in direction_map:
            raise ValueError(
                "Path contains cells that are not directly adjacent."
            )

        directions.append(direction_map[movement])

    return "".join(directions)

# Fonksiyonun yazacağı bütün bilgileri dışarıdan veriyoruz. Böylece ayar
# dosyasını tekrar okumasına veya labirent üretmesine gerek kalmıyor. Tek
# görevi sonucu dosyaya yazmak.


def write_maze(
    file_path: str,
    grid: list[list[int]],
    entry: tuple[int, int],
    exit_position: tuple[int, int],
    path: list[tuple[int, int]],
) -> None:
    """Write maze walls, endpoints, and solution to a text file."""
    directions = path_to_directions(path)

    with open(
        file_path,
        "w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:
        for row in grid:
            hexadecimal_row = "".join(
                f"{cell:X}" for cell in row
            )
            output_file.write(hexadecimal_row + "\n")

        output_file.write("\n")
        output_file.write(f"{entry[0]},{entry[1]}\n")
        output_file.write(
            f"{exit_position[0]},{exit_position[1]}\n"
        )
        output_file.write(directions + "\n")
