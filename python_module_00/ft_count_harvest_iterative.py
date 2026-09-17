def ft_count_harvest_iterative():
    day_count = int(input("Days until harvest: "))
    start = 1
    for start in range(1, day_count + 1):
        print(f"Day {start}")
    print("Harvest time!")
