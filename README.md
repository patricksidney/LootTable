# LootTable

## Description
LootTable is a Python library that provides a simple and flexible implementation of a Loot Table.

## Installation
You can easily install LootTable using pip:
```bash
pip install loottable
```

## Example

```python
from loottable import LootTable, DropList

# Create three Drop Lists
drops_1 = DropList(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"])
drops_2 = DropList(["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
drops_3 = DropList(["*"])

# Create a LootTable with up to 100 possible drop options at a 1% chance each
loot_table = LootTable(granularity=100)

# Add loot tables with weighted chances
# In this case, drops_1 has a 30% chance, drops_2 has a 20% chance, and drops_3 has a 1% chance,
# with a 49% chance of no drops.
loot_table.add(drops_1, 30)
loot_table.add(drops_2, 20)
loot_table add(drops_3, 1)

while True:
    res = loot_table.select_drop()
    if res == "*":
        print("Winner!")
        break
    elif res is not None:
        print(res)
```

## Specifications

### `DropList([])`

`DropList` is a simple class that represents a list of drop options. These can be any type of object, as long as they are valid.

#### `DropList.select_drop()`
This method returns a random drop from the `DropList`. It can be useful when you want to re-roll a drop from the list.

---

### `LootTable(**kwargs)`

`LootTable` is the main loot table class.

##### **Parameters**:
- `seed` (optional) - A unique starting seed for the loot table, defaults to the Python default seed.
- `granularity` (optional) - The defined granularity for the loot table, defaults to 100.

#### `LootTable.add(DropList, weight)`
Adds a `DropList` to the loot table.

##### **Parameters**:
 - `DropList` - The `DropList` you want to add to the loot table.
 - `weight` - An integer specifying the odds of selecting this table. The odds are calculated as `weight / granularity`.

#### `LootTable.select_drop()`
This method selects a random drop based on the configuration of your loot table.

---

## Future Features
 - Removal of drop lists from existing loot tables
 - Quick JSON loading
 - ??? (We are open to suggestions)
```

This revised document enhances readability and maintains a professional tone throughout. Feel free to adapt it further to suit your needs.