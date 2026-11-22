import importlib


def check_reagent(name: str, description: str) -> bool:
    try:
        module = importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - {description}")
        return False
    print(f"[OK] {name} ({module.__version__}) - {description}")
    return True


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    all_present = True
    if not check_reagent("pandas", "Data manipulation ready"):
        all_present = False
    if not check_reagent("numpy", "Numerical computation ready"):
        all_present = False

    print("\npip vs Poetry:")
    print("  requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.\n")

    if all_present:
        print("All reagents present and accounted for.")
    else:
        print("Some reagents are missing. Install them with:")
        print("  pip:    pip install -r ex0/requirements.txt")
        print("  Poetry: poetry install")


if __name__ == "__main__":
    main()