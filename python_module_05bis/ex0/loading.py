import importlib


def check_reagent(name: str, description: str) -> bool:
    try:
        module = importlib.import_module(name)
        version: str = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {description}")
        return True
    except ImportError:
        print(f"[MISSING] {name} - {description}")
        return False


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    reagents: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
    ]

    all_present: bool = True
    for name, desc in reagents:
        if not check_reagent(name, desc):
            all_present = False

    print("\npip vs Poetry:")
    print(
        "  requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "  pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved"
    )
    print("  versions in poetry.lock so every install is identical.\n")

    if all_present:
        print("All reagents present and accounted for.")
    else:
        print("WARNING: Missing reagents detected!")
        print("To install with pip:")
        print("  pip install -r ex0/requirements.txt")
        print("To install with Poetry:")
        print("  poetry install")


if __name__ == "__main__":
    main()
