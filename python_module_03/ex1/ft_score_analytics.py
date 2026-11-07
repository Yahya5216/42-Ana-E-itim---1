
import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    numbers: list[int] = []
    for i in sys.argv[1:]:
        try:
            numbers.append(int(i))
        except ValueError:
            print(f"Invalid parameter: '{i}'")

    count = len(numbers)
    if count == 0:
        print("No scores provided. Usage: "
              f"python3 {sys.argv[0]} <score1> <score2> ...")
        return
    print(f"Scores processed: {numbers}")

    print(f"Total players: {count}")
    sum_value = sum(numbers)
    print(f"Total score: {sum_value}")
    average_value = sum_value / count
    print(f"Average score: {average_value}")
    max_value = max(numbers)
    print(f"High score: {max_value}")
    min_value = min(numbers)
    print(f"Low score: {min_value}")
    score_range = max_value - min_value
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
