import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")

    all_cap: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_cap}")

    only_cap: list[str] = [n for n in players if n[:1].isupper()]
    print(f"New list of capitalized names only: {only_cap}\n")

    scores: dict[str, int] = {n: random.randint(0, 1000) for n in all_cap}
    print(f"Score dict: {scores}")

    avg: float = round(sum([scores[n] for n in scores]) / len(scores), 2)
    print(f"Score average is {avg}")

    high: dict[str, int] = {n: scores[n] for n in scores if scores[n] > avg}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
