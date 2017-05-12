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

def fill_empty_rows_in_matrix(matrix,thief):
    for i in range(len(thief.item_list)):
        item=thief.item_list[i]
        for j in range(len(matrix[1])):
            if j<item.size:
                matrix[i+1][j]=matrix[i][j]
            else:
                matrix[i+1][j]=max(matrix[i][j-item.size]+item.value,matrix[i][j])

def print_output(matrix,thief):
    i,j=len(matrix)-1,len(matrix[0])-1
    value=matrix[i][j]
    output=[]

    while i!=0:
        next_value=matrix[i-1][j]
        if next_value==value:
            output.append(0)
            i-=1
        else:
            output.append(1)
            i-=1
            j-=thief.item_list[i].size
            value=matrix[i][j]

    output=output[::-1]

    print()
    print("Value: {}, X: {}".format(matrix[-1][-1],output))

def APD(thief):
    matrix=generate_empty_matrix(thief)
    fill_empty_rows_in_matrix(matrix,thief)
    print_matrix(matrix)
    print_output(matrix,thief)
