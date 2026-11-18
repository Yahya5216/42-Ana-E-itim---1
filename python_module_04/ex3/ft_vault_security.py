
def secure_archive(
    filename: str, action: str | int = "r", content: str = ""
) -> tuple[bool, str]:
    try:
        if action in ("r", "read", 0):
            with open(filename, "r") as file:
                return (True, file.read())
        elif action in ("w", "write", 1):
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action specified: {action}")
    except OSError as e:
        return (False, f"{e}")


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    success, read_content = secure_archive("ancient_fragment.txt", "r")
    print((success, read_content))

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", "w", read_content))


if __name__ == "__main__":
    ft_vault_security()
