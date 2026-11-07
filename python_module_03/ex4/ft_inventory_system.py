
import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for data in sys.argv[1:]:
        try:
            item_name, quantity = data.split(':')
        except ValueError:
            print(f"Error - invalid parameter '{data}'")
            continue
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            inventory.update({item_name: int(quantity)})
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    print(f"Got inventory: {inventory}")
    if len(inventory) == 0:
        return
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    if total != 0:
        for item in inventory:
            rate = round(inventory[item] /
                         total * 100, 1)
            print(f"Item {item} represents {rate}%")
    most = items[0]
    least = items[0]
    for item in inventory:
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
