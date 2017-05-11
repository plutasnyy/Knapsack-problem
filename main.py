from load_data import *
from class_file import *
def print_input(thief):
    print(thief.knapsack.capacity)
    for i in thief.item_list:
        print(i.value,i.size)
ruckasck_capacity,items=load_data()
thief=Thief(Knapsack(ruckasck_capacity),items)
print_input(thief)
