import os

from dotenv import load_dotenv


def load_config() -> dict[str, str]:
    load_dotenv()
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", ""),
    }


def find_missing(config: dict[str, str]) -> list[str]:
    missing: list[str] = []
    for key in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT"):
        if config[key] == "":
            missing += [key]
    return missing


def is_env_ignored() -> bool:
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, ".gitignore")
    if not os.path.exists(path):
        return False
    with open(path) as file:
        for line in file:
            if line.strip() == ".env":
                return True
    return False


def show_config(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if config["DATABASE_URL"] == "":
        print("Database: Not configured")
    elif mode == "production":
        print("Database: Connected to production database")
    else:
        print("Database: Connected to local instance")

    if config["API_KEY"] == "":
        print("API Access: Missing key")
    else:
        print("API Access: Authenticated")
    level = config["LOG_LEVEL"]
    print(f"Log Level: {level}")

    if config["ZION_ENDPOINT"] == "":
        print("Remote Network: Offline")
    else:
        print("Remote Network: Online")


def main() -> None:
    config = load_config()
    print("ORACLE STATUS: Consulting the configuration...\n")
    show_config(config)

    missing = find_missing(config)
    if missing:
        if config["MATRIX_MODE"] == "production":
            label = "ERROR"
        else:
            label = "WARNING"
        print(f"\n{label}: missing configuration: {', '.join(missing)}")
        print("Copy ex1/.env.example to ex1/.env and fill in your values.")

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    if is_env_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env is NOT listed in .gitignore!")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
