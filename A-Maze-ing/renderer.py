# Terminal gosterimi, renkler ve kullanici etkilesimleri

"""Display a maze in the terminal."""

import re

from mazegen.generator import MazeGenerator, NORTH, WEST, SOUTH, EAST
WALL_COLORS = (
    # Beyaz
    "\033[37m",
    # Kırmızı
    "\033[31m",
    # Yeşil
    "\033[32m",
    # Mavi
    "\033[34m",
)
RESET = "\033[0m"
# Yeşil
ENTRY_COLOR = "\033[32m"
# Kırmızı
EXIT_COLOR = "\033[31m"
# Sarı
PATH_COLOR = "\033[33m"
# Camgöbeği
PATTERN_COLOR = "\033[36m"


def junction_character(
    up: bool,
    right: bool,
    down: bool,
    left: bool,
) -> str:
    """Choose a character for the lines meeting at a junction."""
    characters = {
        (False, False, False, False): " ",
        (True, False, False, False): "╵",
        (False, True, False, False): "╶",
        (False, False, True, False): "╷",
        (False, False, False, True): "╴",
        (True, False, True, False): "│",
        (False, True, False, True): "─",
        (False, True, True, False): "┌",
        (False, False, True, True): "┐",
        (True, True, False, False): "└",
        (True, False, False, True): "┘",
        (True, True, True, False): "├",
        (True, False, True, True): "┤",
        (False, True, True, True): "┬",
        (True, True, False, True): "┴",
        (True, True, True, True): "┼",
    }

    return characters[(up, right, down, left)]


def render_maze(
    maze: MazeGenerator,
    entry: tuple[int, int],
    exit_position: tuple[int, int],
    path: list[tuple[int, int]] | None = None,
    color_index: int = 0,
) -> None:
    """Print maze walls, endpoints, pattern, and an optional solution."""
    wall_color = WALL_COLORS[color_index % len(WALL_COLORS)]
    path_cells = set(path) if path is not None else set()
    pattern_cells = maze.get_pattern_cells()

    # Draw walls first, then paint the closed pattern as solid digits.
    lines: list[str] = []
    for y in range(maze.height):
        top_line = ""
        middle_line = ""

        for x in range(maze.width):
            position = (x, y)

            top_line += wall_color + get_junction(maze, x, y) + RESET

            if maze.has_wall(x, y, NORTH):
                top_line += wall_color + "───" + RESET
            else:
                top_line += "   "

            if maze.has_wall(x, y, WEST):
                middle_line += wall_color + "│" + RESET
            else:
                middle_line += " "

            if position == entry:
                symbol = ENTRY_COLOR + "S" + RESET
            elif position == exit_position:
                symbol = EXIT_COLOR + "E" + RESET
            elif position in pattern_cells:
                symbol = PATTERN_COLOR + "███" + RESET
            elif position in path_cells:
                symbol = PATH_COLOR + "·" + RESET
            else:
                symbol = " "

            if position in pattern_cells:
                middle_line += symbol
            else:
                middle_line += f" {symbol} "

        top_line += (
            wall_color + get_junction(maze, maze.width, y) + RESET
        )
        middle_line += wall_color + "│" + RESET

        lines.append(top_line)
        lines.append(middle_line)

    bottom_line = ""

    for x in range(maze.width):
        bottom_line += get_junction(maze, x, maze.height)
        bottom_line += "───"

    bottom_line += get_junction(maze, maze.width, maze.height)
    lines.append(wall_color + bottom_line + RESET)

    # ANSI sequences have no display width; remove them before overlaying
    # the pattern, keeping a separate color for each visible character.
    canvas = [list(re.sub(r"\x1b\[[0-9;]*m", "", line)) for line in lines]
    colors = [[wall_color for _ in row] for row in canvas]

    for x, y in pattern_cells:
        # Keep the cell boundaries visible, as in the subject's example.
        for screen_x in range(4 * x + 1, 4 * x + 4):
            canvas[2 * y + 1][screen_x] = "░"
            colors[2 * y + 1][screen_x] = PATTERN_COLOR

    for y in range(maze.height):
        for x in range(maze.width):
            position = (x, y)
            if position in pattern_cells:
                continue
            if position == entry:
                color = ENTRY_COLOR
            elif position == exit_position:
                color = EXIT_COLOR
            elif position in path_cells:
                color = PATH_COLOR
            else:
                continue
            colors[2 * y + 1][4 * x + 2] = color

    for row, row_colors in zip(canvas, colors):
        print("".join(color + char for char, color in zip(row, row_colors))
              + RESET)


def get_junction(maze: MazeGenerator, x: int, y: int) -> str:
    """Return the wall junction character at a grid corner."""
    up = (
        y > 0
        and (
            maze.has_wall(x, y - 1, WEST)
            if x < maze.width
            else maze.has_wall(x - 1, y - 1, EAST)
        )
    )

    right = (
        x < maze.width
        and (
            maze.has_wall(x, y, NORTH)
            if y < maze.height
            else maze.has_wall(x, y - 1, SOUTH)
        )
    )

    down = (
        y < maze.height
        and (
            maze.has_wall(x, y, WEST)
            if x < maze.width
            else maze.has_wall(x - 1, y, EAST)
        )
    )

    left = (
        x > 0
        and (
            maze.has_wall(x - 1, y, NORTH)
            if y < maze.height
            else maze.has_wall(x - 1, y - 1, SOUTH)
        )
    )

    return junction_character(up, right, down, left)
