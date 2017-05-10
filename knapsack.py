class Item(object):
    def __init__(self, value, size):
        self.value=value
        self.size=size

class Knapsack(object):
    def __init__(self, capacity):
        self.capacity=capacity

knapsack=Knapsack(6)
item=Item(3,4)
print(knapsack.capacity, item.value, item.size)
