import os
import site
import sys


def main() -> None:
    in_venv: bool = (
        sys.prefix != sys.base_prefix
        or os.environ.get("VIRTUAL_ENV") is not None
    )

    if not in_venv:
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!")
        print(
            "Every reagent you install here leaks into the whole system.\n"
        )
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        env_path: str = os.environ.get("VIRTUAL_ENV", sys.prefix)
        env_name: str = os.path.basename(os.path.normpath(env_path))
        site_pkgs: list[str] = site.getsitepackages()
        pkg_path: str = site_pkgs[-1] if site_pkgs else env_path

        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.\n")
        print("Reagent installation path:")
        print(pkg_path)


if __name__ == "__main__":
    main()
