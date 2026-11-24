"""Ayar dosyasini okuma ve dogrulama islemleri."""
from dataclasses import dataclass


# burda initle self.width = width yani her biri için yapmayalım otomatikmen
# dataclass yapsın
@dataclass
class MazeConfig:
    """Store the validated maze configuration."""

    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    # ilk baştaki int ya da none olabilir türü = none demesinin sebebi
    # verilmezse none olsun
    seed: int | None = None


def read_config_file(file_path: str) -> dict[str, str]:
    """Read configuration entries as text."""
    settings: dict[str, str] = {}

    with open(file_path, "r", encoding="utf-8") as config_file:
        for line_number, line in enumerate(config_file, start=1):
            line = line.strip()

            # satır boş mu yoksa yorum satırı mı var
            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(
                    f"Line {line_number}: expected KEY=VALUE."
                )

            key, value = line.split("=", 1)
            key = key.strip().upper()
            value = value.strip()

            if not key or not value:
                raise ValueError(
                    f"Line {line_number}: empty key or value."
                )

            if key in settings:
                raise ValueError(
                    f"Line {line_number}: duplicate key '{key}'."
                )

            settings[key] = value

    return settings


def parse_positive_int(value: str, key: str) -> int:
    """Convert a configuration value to a positive integer."""
    try:
        number = int(value)
    except ValueError:
        raise ValueError(
            f"{key} must be an integer."
            # yeni hatanın gösteriminde önceki dönüşüm hatasının zincirini
            # gizler inte dönüştüremediği için zaten hata oluşacak onu
            # göstermeyip kendi
            # hatamızı gösteriyoruz gizliyoruz yani onu
        ) from None

    if number <= 0:
        raise ValueError(
            f"{key} must be greater than zero."
        )

    return number


def parse_coordinates(value: str, key: str) -> tuple[int, int]:
    """Convert an x,y configuration value to a coordinate pair."""
    parts = value.split(",")

    if len(parts) != 2:
        raise ValueError(
            f"{key} must contain two coordinates: x,y."
        )

    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        raise ValueError(
            f"{key} coordinates must be integers."
        ) from None

    return x, y

# perfecti kontrol ediyoruz


def parse_bool(value: str, key: str) -> bool:
    """Convert a True or False configuration value to a boolean."""
    normalized = value.lower()

    if normalized == "true":
        return True

    if normalized == "false":
        return False

    raise ValueError(
        f"{key} must be True or False."
    )


def validate_required_keys(settings: dict[str, str]) -> None:
    """Check that all required configuration keys are present."""
    required_keys = (
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT",
    )

    for key in required_keys:
        if key not in settings:
            raise ValueError(
                f"Missing required configuration key: {key}."
            )


def load_config(file_path: str) -> MazeConfig:
    """Read configuration values and create a configuration object."""
    settings = read_config_file(file_path)
    validate_required_keys(settings)

    # settings de ilki değer diğeri ayar adı 20, width gibi
    width = parse_positive_int(settings["WIDTH"], "WIDTH")
    height = parse_positive_int(settings["HEIGHT"], "HEIGHT")
    entry = parse_coordinates(settings["ENTRY"], "ENTRY")
    exit_position = parse_coordinates(settings["EXIT"], "EXIT")
    perfect = parse_bool(settings["PERFECT"], "PERFECT")

    seed: int | None = None

    if "SEED" in settings:
        try:
            seed = int(settings["SEED"])
        except ValueError:
            raise ValueError(
                "SEED must be an integer."
            ) from None

    config = MazeConfig(
        width=width,
        height=height,
        entry=entry,
        exit=exit_position,
        output_file=settings["OUTPUT_FILE"],
        perfect=perfect,
        seed=seed,
    )
    validate_positions(config)
    return config


def validate_positions(config: MazeConfig) -> None:
    """Check that entry and exit are distinct and inside the maze."""
    positions = (
        ("ENTRY", config.entry),
        ("EXIT", config.exit),
    )

    for key, position in positions:
        x, y = position

        if not (0 <= x < config.width and 0 <= y < config.height):
            raise ValueError(
                f"{key} must be inside the maze boundaries."
            )

    if config.entry == config.exit:
        raise ValueError(
            "ENTRY and EXIT must be different."
        )
