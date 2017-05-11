def generate_empty_matrix(thief):
    temp=[]
    for i in range(len(thief.item_list)):
        X=[]
        for j in range(thief.knapsack.capacity):
            X.append(0)
        temp.append(X)
    return temp

def print_matrix(matrix):
    print()
    for i in matrix:
        print(i)

def fill_first_row(matrix,thief):
    item = thief.item_list[0]
    for i in range(len(matrix[0])):
        if i+1 < item.size:
            matrix[0][i]=0
        else:
            matrix[0][i]=item.value

def fill_empty_row_in_matrix(matrix,thief):
    for i in range(1,len(thief.item_list)):
        item=thief.item_list[i]
        for j in range(len(matrix[1])):
            if j+1<item.size:
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i-1][j-item.size+1]+item.value)

def APD(thief):
    matrix=generate_empty_matrix(thief)
    fill_first_row(matrix,thief)
    print_matrix(matrix)
    fill_empty_row_in_matrix(matrix,thief)
    print_matrix(matrix)
