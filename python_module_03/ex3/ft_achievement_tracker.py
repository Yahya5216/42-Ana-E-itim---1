
import random


all_achievements: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    random_nbr = random.randint(4, 9)
    return set(random.sample(all_achievements, random_nbr))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    players: list[tuple[str, set[str]]] = []
    sets: list[set[str]] = []
    for name in names:
        achievements = gen_player_achievements()
        players.append((name, achievements))
        sets.append(achievements)
        print(f"Player {name}: {achievements}")

    print(f"\nAll distinct achievements: {set.union(*sets)}")
    print(f"\nCommon achievements: {set.intersection(*sets)}\n")

    for name, achievements in players:
        others: set[str] = set()
        for other_name, other_achievements in players:
            if name != other_name:
                others = others.union(other_achievements)
        print(f"Only {name} has: {achievements.difference(others)}")

    print()
    all_set = set(all_achievements)
    for name, achievements in players:
        print(f"{name} is missing: {all_set.difference(achievements)}")


if __name__ == "__main__":
    main()
