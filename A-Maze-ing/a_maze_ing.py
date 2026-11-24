"""Run the A-Maze-ing application."""

import sys

from config_parser import load_config
from mazegen.generator import MazeGenerator
from maze_writer import write_maze
from renderer import render_maze


RESET = "\033[0m"

# Ayarları okuyup doğruluyoruz.
# Bu boyutlara sahip üreticiyi oluşturuyoruz.
# Desenin nerede olacağını hesaplıyoruz.
# Giriş veya çıkış desen üzerindeyse hata veriyoruz.
# Kontroller geçerse labirenti üretiyoruz.


def main() -> int:
    """Load maze settings and report configuration errors."""
    if len(sys.argv) != 2:
        print(
            "Usage: python3 a_maze_ing.py config.txt",
            file=sys.stderr,
        )
        return 1

    try:
        config = load_config(sys.argv[1])

        maze = MazeGenerator(
            width=config.width,
            height=config.height,
            seed=config.seed,
        )

        pattern_cells = maze.get_pattern_cells()

        if not pattern_cells:
            print(
                "Warning: maze is too small for the 42 pattern; "
                "the pattern will be omitted.",
                file=sys.stderr,
            )

        if (
            config.entry in pattern_cells
            or config.exit in pattern_cells
        ):
            raise ValueError(
                "ENTRY and EXIT must not overlap the 42 pattern."
            )

        if config.perfect:
            maze.generate()
        else:
            maze.generate_playable()

        path = maze.solve(config.entry, config.exit)

        write_maze(
            file_path=config.output_file,
            grid=maze.grid,
            entry=config.entry,
            exit_position=config.exit,
            path=path,
        )

    except (
        OSError, ValueError, UnicodeError, MemoryError, OverflowError
    ) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    show_path = False
    color_index = 0

    try:
        while True:
            if sys.stdout.isatty():
                print("\033[2J\033[H", end="")
            render_maze(
                maze,
                config.entry,
                config.exit,
                path if show_path else None,
                color_index=color_index,
            )

            if not pattern_cells:
                print("42 pattern omitted: maze is too small.")

            command = input(
                "[r] Regenerate | [p] Solution | [c] Color | [q] Quit: "
            ).strip().lower()

            if command == "q":
                return 0

            if command == "p":
                show_path = not show_path

            # bununla yeni labirent üretiyoruz
            elif command == "r":
                if config.perfect:
                    maze.generate()
                else:
                    maze.generate_playable()
                path = maze.solve(config.entry, config.exit)

                write_maze(
                    file_path=config.output_file,
                    grid=maze.grid,
                    entry=config.entry,
                    exit_position=config.exit,
                    path=path,
                )

            elif command == "c":
                color_index += 1

            else:
                print("Unknown command. Use r, p, c, or q.")

    except (
        OSError, ValueError, UnicodeError, MemoryError, OverflowError
    ) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
