def generate_empty_matrix(thief):
    temp=[]
    for i in range(len(thief.item_list)+1):
        X=[]
        for j in range(thief.knapsack.capacity+1):
            X.append(0)
        temp.append(X)
    return temp

def print_matrix(matrix):
    print()
    for i in matrix:
        print(i)

def fill_first_row(matrix,thief):
    item = thief.item_list[0]
    for i in range(1,len(matrix[0])):
        if i < item.size:
            matrix[1][i]=0
        else:
            matrix[1][i]=item.value

def fill_empty_row_in_matrix(matrix,thief):
    for i in range(1,len(thief.item_list)):
        item=thief.item_list[i]
        for j in range(len(matrix[1])):
            if j<item.size:
                matrix[i+1][j]=matrix[i][j]
            else:
                matrix[i+1][j]=max(matrix[i][j-item.size]+item.value,matrix[i][j])

def APD(thief):
    matrix=generate_empty_matrix(thief)
    fill_first_row(matrix,thief)
    print_matrix(matrix)
    fill_empty_row_in_matrix(matrix,thief)
    print_matrix(matrix)
