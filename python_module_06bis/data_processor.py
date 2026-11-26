from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._storage) == 0:
            raise IndexError("No data available to output")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, (int, float)) or isinstance(
                    item, bool
                ):
                    return False
            return True
        return False

    def ingest(
        self,
        data: int | float | list[int] | list[float] | list[int | float],
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._total_processed, str(item)))
                self._total_processed += 1
        else:
            self._storage.append((self._total_processed, str(data)))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._total_processed, item))
                self._total_processed += 1
        else:
            self._storage.append((self._total_processed, data))
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def _is_valid_log(self, item: Any) -> bool:
        if not isinstance(item, dict) or len(item) == 0:
            return False
        for key, value in item.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True

    def _format_log(self, entry: dict[str, str]) -> str:
        if "log_level" in entry and "log_message" in entry:
            return f"{entry['log_level']}: {entry['log_message']}"
        parts: list[str] = []
        for value in entry.values():
            parts.append(value)
        return ": ".join(parts)

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_log(data)
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not self._is_valid_log(item):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for entry in data:
                formatted = self._format_log(entry)
                self._storage.append((self._total_processed, formatted))
                self._total_processed += 1
        else:
            formatted = self._format_log(data)
            self._storage.append((self._total_processed, formatted))
            self._total_processed += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as err:
        print(f" Got exception: {err}")
    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_data}")
    num_proc.ingest(num_data)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    print()
    print("Testing Text Processor...")
    text_proc = TextProcessor()
    print(f" Trying to validate input '42': {text_proc.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_data}")
    text_proc.ingest(text_data)
    print(" Extracting 1 value...")
    rank, value = text_proc.output()
    print(f" Text value {rank}: {value}")

    print()
    print("Testing Log Processor...")
    log_proc = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {log_data}")
    log_proc.ingest(log_data)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log_proc.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
