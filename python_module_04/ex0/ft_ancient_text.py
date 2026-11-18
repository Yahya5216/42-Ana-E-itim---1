import sys
import typing


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    try:
        file = open(filename, "r")
        text: str = file.read()
        print("---\n")
        print(text)
        print("---")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
