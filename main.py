from load_data import *
from class_file import *
from AW import *
from APD import *
from generate_random_data import *

def print_input(thief):
    print(thief.knapsack.capacity)
    for i in thief.item_list:
        print(i.value,i.size)
    print()

ruckasck_capacity,items=load_data()
thief=Thief(Knapsack(ruckasck_capacity),items)
print_input(thief)


AW(thief)
APD(thief)
