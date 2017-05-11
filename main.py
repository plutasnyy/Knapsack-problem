from load_data import *
from class_file import *

ruckasck_capacity,items=load_data()
thief=Thief(Knapsack(ruckasck_capacity),items)
print(thief.item_list[0].value)
