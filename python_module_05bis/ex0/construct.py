import os
import site
import sys


def show_out() -> None:
    print("LABORATORY STATUS: You are working in the open\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def show_in() -> None:
    env_path = sys.prefix
    env_name = os.path.basename(env_path)
    packages_list = site.getsitepackages()
    packages_path = packages_list[0]

    print("LABORATORY STATUS: The laboratory is sealed\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}\n")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.\n")
    print("Reagent installation path:")
    print(packages_path)


def main() -> None:
    if sys.prefix != sys.base_prefix:
        show_in()
    else:
        show_out()


if __name__ == "__main__":
    main()
