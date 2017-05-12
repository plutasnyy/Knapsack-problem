from class_file import Item
from random import randint

def generate_random_data(capacity,quantity_of_items):
    data_file=open("data.txt","w")

    data_file.write(str(capacity))
    for i in range(quantity_of_items):
        data_file.write("\n{} {}".format(randint(1,10),randint(1,10)))

    data_file.close()

def input_pair():
    first,second="a a".split()
    while(first.isdigit()==False or second.isdigit()==False):
            dane=input().split()
            if(len(dane)==2):
                first,second=dane[0],dane[1]
                if first<='0' or second<='0':
                    first='a'
    print("OK")
    return int(first),int(second)

def manual_input():
    print("Dane wprowadzaj w formacie \"X X\", zaakceptowane dane sygnalizowane sa przez OK")
    print("Poczatkowo wprowadz pojemnosc plecaka i ilosc elementow")
    print("Nastepnie wprowadzaj wielkosc i wartosc przedmiotu")

    capacity,quantity_of_items=input_pair()
    item_list=[]

    for i in range(quantity_of_items):
        size,value=input_pair()
        item_list.append(Item(size,value))

    return capacity,item_list

def load_data():
    try:
        data_file=open("data.txt","r")
        data=data_file.read().split("\n")
        capacity=int(data[0])

        data.remove(data[0])
        if(data[-1]==""):
            data.remove(data[-1])

        item_list=[Item(int(i),int(j)) for i,k,j in data] #k is null 'a b'
        data_file.close()
        return capacity,item_list

    except FileNotFoundError:
        return  manual_input()
