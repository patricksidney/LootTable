import random

class LootTable:
    def __init__(self,granularity=100,seed=None):
        self.granularity = granularity
        self.drop_lists = []
        if seed != None:
            random.seed(seed)
        self.validated = False

    def add(self,drop_list, weight):
        self.drop_lists.append((drop_list, weight))

    def select_drop(self):
        if self.validated == False:
            self.validate()
        r = random.randint(0,self.granularity)
        for drop_list, weight in self.drop_lists:
            if r < weight:
                return drop_list.select_drop()
            r -= weight
        return None

    def validate(self):
        total_weight = 0
        for drop_list, weight in self.drop_lists:
            total_weight += weight
        if total_weight > self.granularity:
            raise Exception("Invalid LootTable: total weight is too high")
        if total_weight == 0:
            raise Exception("Invalid LootTable: no valid drops")
        self.validated = True

class DropList:
    def __init__(self, drops):
        self.drops = drops

    def select_drop(self):
        r = random.randint(0,len(self.drops)-1)
        return self.drops[r]