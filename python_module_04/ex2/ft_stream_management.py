import sys
import typing


def print_error(message: str) -> None:
    print(f"[STDERR] {message}", file=sys.stderr)


def ask_filename() -> str:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    return sys.stdin.readline().strip()


def read_archive(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    text: str | None = None
    try:
        file = open(filename, "r")
        text = file.read()
        print("---\n")
        print(text)
        print("---")
    except OSError as e:
        print_error(f"Error opening file '{filename}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")
    return text


def transform(text: str) -> str:
    lines: list[str] = text.splitlines()
    result: str = ""
    for line in lines:
        result += line + "#\n"
    return result


def save_archive(filename: str, data: str) -> None:
    print(f"Saving data to '{filename}'")

    file: typing.IO[str] | None = None
    try:
        file = open(filename, "w")
        file.write(data)
        print(f"Data saved in file '{filename}'.")
    except OSError as e:
        print_error(f"Error opening file '{filename}': {e}")
        print("Data not saved.")
    finally:
        if file is not None:
            file.close()


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    text: str | None = read_archive(sys.argv[1])
    if text is None:
        return

    new_text: str = transform(text)
    print("\nTransform data:")
    print("---\n")
    print(new_text)
    print("---")

    filename = ask_filename()
    if filename == "":
        print("Not saving data.")
    else:
        save_archive(filename, new_text)


if __name__ == "__main__":
    ft_archive_creation()
