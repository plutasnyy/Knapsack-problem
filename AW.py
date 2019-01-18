def AW(thief):
    for ind, item in enumerate(thief.item_list):
        item.coef = item.value / item.size
        item.ind = ind
        item.packed = False
    thief.item_list = sorted(thief.item_list, key=lambda x: x.coef, reverse=True)
    current_size = 0
    value = 0
    i = 0
    while current_size <= thief.knapsack.capacity and i < len(thief.item_list):
        if current_size + thief.item_list[i].size <= thief.knapsack.capacity:
            current_size += thief.item_list[i].size
            value += thief.item_list[i].value
            thief.item_list[i].packed = True
        i += 1
    thief.item_list = sorted(thief.item_list, key=lambda x: x.ind)
    X = [int(i.packed) for i in thief.item_list]
    print('Value: {}, X: {}'.format(value, X))
