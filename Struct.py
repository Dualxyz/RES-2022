from ast import Del
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
        # print(self.hc.Receiver_Property.code);
        # print(self.hc.Receiver_Property.value);


        if(code == "CODE_ANALOG" or code == "CODE_DIGITAL"):
            self.dataset = "DATASET1";
        elif(code == "CODE_CUSTOM" or code == "CODE_LIMITSET"):
            self.dataset = "DATASET2";
        elif(code == "CODE_SINGLENOE" or code == "CODE_MULTIPLENODE"):
            self.dataset = "DATASET3";
        elif(code == "CODE_CONSUMER" or code == "CODE_SOURCE"):
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

class DeltaCD:
    def __init__(self, CD):
        temp_list = [];
        self.lista_add = [];
        self.lista_update = [];
        
#Okej, imaš neku glavnu kolekciju koja će čuvati svu istoriju pristiglih posataka
#  i te dve što si naveo "add" i "update". 
# Za sve nove podatke koji pristižu proveravaš da lo već postoje u glavnoj,
#  ako da - dodaješ je u "update" ako ne - u "add". 
# I bukvalno posle 10 novo pristiglih podataka te dve kolekcije samo proslediš readeru koji
#  upisuje u bazu

        if(len(self.lista_add) == 0):
            self.lista_add.append(CD);
        else:
            for i in range(0, len(self.lista_add)):
                if(CD.hc.Receiver_Property.code == self.lista_add[i].hc.Receiver_Property.code):
                    print("send to lista_update");
                    self.lista_add[i].hc.Receiver_Property.value = CD.hc.Receiver_Property.value;
                else:
                    self.lista_add.append(CD);
        
        
        # for i in range(0)

        # if self.lista_add == []:
        #     self.lista_add.append(CD);
        # elif 
        # if self.lista_add == 0:
        #     for i in range(0, len(self.lista_add)):
        #         if(CD.hc.Receiver_Property.code in self.lista_add[i].hc.Receiver_Property.code):
        #             self.lista_add.append(CD);
        #             print("update and: " + self.lista_add[i].hc.Receiver_Property.code);
        #         else:
        #             print("Don't update");
        #             self.lista_update.append(CD);
        # else:
        #     print("list empty");
        #print("Whatever + " + str(CD.hc.Receiver_Property.code));
        #print("This is good: " + str(self.lista_add[0].hc.Receiver_Property.code));


        # lista.append(Collection_Description);
        # List<Collection_Description> update;
        # AddItem:List[Collection_Description] = list()       #List for all new items
        # UpdateItem:List[Collection_Description] = list()    #List for items that didn't already exist
        # BufferItem:List[Collection_Description] = list()    #List for items that existed but got their value changed



if __name__ == "__main__":
    id = random.randint(1,100);
    packets = [];
    packet = Collection_Description(id, "CODE_SOURCE", "12");
    packets.append(packet)
    deltaCD = DeltaCD(packets);
    print("wat " + packet.dataset);
    print(f"Deltacd: {deltaCD.lista_add[0].hc.Receiver_Property.code}");

    # if(packet.dataset == "DATASET1"):
    #     print(f"DATASET1. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
    #     #LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_1.\n");
    # elif(packet.dataset == "DATASET2"):
    #     print(f"DATASET2. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
    #     #LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_2.\n");
    # elif(packet.dataset == "DATASET3"):
    #     print(f"DATASET3. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
    #     #LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_3.\n");
    # elif(packet.dataset == "DATASET4"):
    #     print(f"DATASET4. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
    #     #LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_4.\n");
    # else:
    #     print("Error...");