def return_bin(i,quantity_of_items):
    number=bin(i)[2:] #number as binary
    combination=[0 for i in range(quantity_of_items)]
    for i in range(len(number)):
        combination[-i-1]+=int(number[-i-1])
    return combination

def calculate_solution(X,thief):
    value=0
    size=0
    for i in range(len(thief.item_list)):
        value+=thief.item_list[i].value*X[i]
        size+=thief.item_list[i].size*X[i]
    return value,size

def AW(thief):
    max_value=0
    best_solution=[]

    quantity_of_items=len(thief.item_list)
    combinations_number=2**quantity_of_items

    for i in range(combinations_number):
        X=return_bin(i,quantity_of_items)
        current_value,size=calculate_solution(X,thief)

        if current_value > max_value and size<=thief.knapsack.capacity:
            max_value=current_value
            best_solution=X

    print("Value: ",max_value,"X: ", best_solution)
