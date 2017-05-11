from class_file import Item

def input_pair():
    first,second="a a".split()
    while(first.isdigit()==False or second.isdigit()==False):
            dane=input().split()
            if(len(dane)==2):
                first,second=dane[0],dane[1]
                pom=str(self.vertices_count)
                if first<='0' or second<='0':
                    first='a'
    print("OK")
    return int(first),int(second)

def manual_input():
    print("Dane wprowadzaj w formacie \"X X\", zaakceptowane dane sygnalizowane sa przez OK")
    print("Poczatkowo wprowadz pojemnosc plecaka i ilosc elementow")
    print("Nastepnie wprowadzaj wielkosc i wartosc przedmiotu")
    capacity,quantity_of_items=input_pair
    item_list=[]
    for i in range(int(quantity_of_items)):
        size,value=input_pair
        item_list.append(Item(size,value))
    return capacity,item_list

def load_data():
    try:
        file=open("data.txt","r")
        data=plik.read().split("\n")
        capacity=int(data[0])
        item_list=[Item(int(i),int(j)) for i,j in data.split()]
        file.close()
        return capacity,item_list
    except FileNotFoundError:
        return  manual_input()
