class Item(object):
    def __init__(self, size, value):
        self.value=value
        self.size=size

class Knapsack(object):
    def __init__(self, capacity):
        self.capacity=capacity

class Thief(object):
    def __init__(self,knapsack,item_list):
        self.knapsack=knapsack
        self.item_list=item_list
