from loottable import LootTable, DropList


drops_1 = DropList(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"])
drops_2 = DropList(["P","Q","R","S","T","U","V","W","X","Y","Z"])
drops_3 = DropList(["*"])

loot_table = LootTable(granularity=100)

loot_table.add(drops_1, 30)
loot_table.add(drops_2, 20)
loot_table.add(drops_3, 1)

while True:
    res = loot_table.select_drop()
    if res == "*":
        print("Winner!")
        break
    else:
        if res!= None:
            print(res)
