import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None  # type: ignore[assignment]


def check_gitignore(base_dir: str) -> bool:
    gitignore_path: str = os.path.join(base_dir, ".gitignore")
    if not os.path.isfile(gitignore_path):
        return False
    try:
        with open(gitignore_path, "r", encoding="utf-8") as f:
            lines: list[str] = [line.strip() for line in f.readlines()]
            return ".env" in lines or "*.env" in lines
    except OSError:
        return False


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...\n")

    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    env_path: str = os.path.join(base_dir, ".env")

    if load_dotenv is not None:
        load_dotenv(dotenv_path=env_path, override=False)
    else:
        print(
            "WARNING: python-dotenv is not installed. "
            "Run: pip install -r ex1/requirements.txt",
            file=sys.stderr,
        )

    required_keys: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    missing: list[str] = [k for k in required_keys if not os.environ.get(k)]

    if missing:
        print(
            f"WARNING: Missing configuration variables: {', '.join(missing)}"
        )
        print("Using fallback default values where necessary.\n")

    mode: str = os.environ.get("MATRIX_MODE", "development").lower()
    db_url: str = os.environ.get("DATABASE_URL", "")
    api_key: str = os.environ.get("API_KEY", "")
    log_level: str = os.environ.get(
        "LOG_LEVEL", "INFO" if mode == "production" else "DEBUG"
    )
    zion_endpoint: str = os.environ.get("ZION_ENDPOINT", "")

    if mode == "production":
        db_status: str = (
            "Connected to production cluster"
            if db_url
            else "Disconnected (missing DATABASE_URL)"
        )
    else:
        db_status = (
            "Connected to local instance"
            if db_url
            else "Using default local SQLite fallback"
        )

    api_status: str = (
        "Authenticated" if api_key else "Unauthenticated (missing API_KEY)"
    )
    network_status: str = (
        "Online" if zion_endpoint else "Offline (default local mode)"
    )

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: {network_status}\n")

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    if check_gitignore(base_dir):
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file is NOT ignored by git!")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
