#! python3
import sys


def fill_inventory(items: list[str]) -> dict[str, int]:
    inventory = {}
    for item in items[1:]:
        key_val = item.split(":")
        try:
            if len(key_val) != 2:
                raise IndexError(item)

            if key_val[0] in inventory:
                raise ValueError(f"Redundant item '{key_val[0]}' - discarding")

            try:
                val = int(key_val[1])
            except ValueError as e:
                raise ValueError(f"Quantity error for '{key_val[0]}': {e}")

            inventory[key_val[0]] = val
        except ValueError as e:
            print(e)

        except IndexError as e:
            print(f"Error - invalid parameter '{e}'")

    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")

    inventory = fill_inventory(sys.argv)
    only_items = list(inventory)
    only_qtd: list[int] = []
    for items in inventory.values():
        only_qtd.append(items)
    total_qtd = sum(only_qtd)
    total_itms = len(only_items)
    most_abdt = ""
    least_abdt = ""

    print(f"\nGot inventory: {inventory}")
    print(f"Item list: {only_items}\n")

    print(f"Total quantity of the {total_itms} items: {total_qtd}")
    for item in inventory:
        if most_abdt == "" or inventory[most_abdt] < inventory[item]:
            most_abdt = item
        if least_abdt == "" or inventory[least_abdt] > inventory[item]:
            least_abdt = item
        print(f"Item {item} represents {round((inventory[item] / total_qtd) * 100, 1)}%")
    print(f"Item most abundant: {most_abdt} with quantity {inventory[most_abdt]}")
    print(f"Item least abundant: {least_abdt} with quantity {inventory[least_abdt]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
