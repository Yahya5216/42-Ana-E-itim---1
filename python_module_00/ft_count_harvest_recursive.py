def count_days(start, day_count):
    if start > day_count:
        return
    print(f"Day {start}")
    count_days(start + 1, day_count)


def ft_count_harvest_recursive():
    day_count = int(input("Days until harvest: "))
    start = 1
    count_days(start, day_count)
