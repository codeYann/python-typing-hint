from typing import Dict


# To use Dict typing you need to params.
# The first one is a type for key and the second one is a type for value
items: Dict[str, float] = {"Arroz": 100.5, "Batata": 15.5, "Feijão": 10.5}


def process_items(items: Dict[str, float]) -> None:
    for items_name, items_price in items.items():
        print(f"{items_name} => {items_price}")


# Write a main function that process items
def main() -> None:
    process_items(items)


main()
