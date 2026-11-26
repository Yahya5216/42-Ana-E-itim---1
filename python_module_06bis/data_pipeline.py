from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._storage: list[tuple[int, str]] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._storage) == 0:
            raise IndexError("No data available to output")
        return self._storage.pop(0)

    def total_processed(self) -> int:
        return self._total_processed

    def remaining_count(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: typing.Any) -> bool:
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
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: typing.Any) -> bool:
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
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def _is_valid_log(self, item: typing.Any) -> bool:
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

    def validate(self, data: typing.Any) -> bool:
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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for _, value in data:
            values.append(value)
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def _escape(self, text: str) -> str:
        text = text.replace("\\", "\\\\")
        text = text.replace('"', '\\"')
        return text

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs: list[str] = []
        for rank, value in data:
            escaped = self._escape(value)
            pairs.append(f'"item_{rank}": "{escaped}"')
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    try:
                        proc.ingest(element)
                        handled = True
                    except Exception as err:
                        print(f"DataStream error - {err}")
                    break
            if not handled:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._processors) == 0:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.name}: total {proc.total_processed()} items "
                f"processed, remaining {proc.remaining_count()} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining_count() == 0:
                    break
                extracted.append(proc.output())
            if len(extracted) > 0:
                plugin.process_output(extracted)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()

    print("Initialize Data Stream...")
    print()
    stream = DataStream()
    stream.print_processors_stats()

    print()
    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print()
    print(f"Send first batch of data on stream: {batch1}")
    print()
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    print()
    stream.print_processors_stats()

    batch2: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print()
    print(f"Send another batch of data: {batch2}")
    print()
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
