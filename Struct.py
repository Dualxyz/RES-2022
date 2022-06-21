import random;
from random import seed
from audioop import add
from turtle import update
from typing import List


class Collection_Description:
    def __init__(self,id,code, value):
        
        self.id = id
        self.dataset = "";
        self.hc = Historical_Collection(code, value);
        print(self.hc.Receiver_Property.code);
        print(self.hc.Receiver_Property.value);

        # code = self.Historical_collection.Receiver_Property.code;
        # value = self.Historical_collection.Receiver_Property.value;

        if(code == "CODE_ANALOG" or code == "CODE_DIGITAL\n"):
            self.dataset = "DATASET1";
        elif(code == "CODE_CUSTOM" or code == "CODE_LIMITSET\n"):
            self.dataset = "DATASET2";
        elif(code == "CODE_SINGLENOE" or code == "CODE_MULTIPLENODE\n"):
            self.dataset = "DATASET3";
        elif(code == "CODE_CONSUMER" or code == "CODE_SOURCE\n"):
            self.dataset = "DATASET4";
        else:
            self.dataset = "ERROR";


class Historical_Collection:
    def __init__(self, code, value):
        self.Receiver_Property = Receiver_Property(code,value)


class Receiver_Property:
    def __init__(self, code, value):
        self.code = code
        self.value = value

# class DeltaCD:
#     def __init__(self):
#         List<Collection_Description> add;
#         lista = [];
#         lista.append(Collection_Description);
#         List<Collection_Description> update;
#         AddItem:List[Collection_Description] = list()       #List for all new items
#         UpdateItem:List[Collection_Description] = list()    #List for items that didn't already exist
#         BufferItem:List[Collection_Description] = list()    #List for items that existed but got their value changed

class Dataset:

    def __init__(self, code, value):
        self.code = code
        self.value = value



if __name__ == "__main__":
    id = random.randint(1,100);
    print(id);
    smt = Collection_Description(id, "CODE_ANALOG", "12");
    print(smt.dataset);