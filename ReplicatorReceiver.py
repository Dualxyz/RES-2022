import threading
from RECEIVER_RECEIVE_FROM_CLASS import REPLICATOR_RECEIVE_FROM;
from RECEIVER_SEND_TO_CLASS import RECEIVER_SEND_TO;
import threading;
from DeltaCD import DeltaCD;
from SEND_TO_LOG import LOG;
from Struct import Collection_Description;

LOG("INFO:root:[REPLICATOR RECEIVER] has started.\n", "127.0.0.1", 9999);

buffer=[];
rrf = threading.Thread(target=REPLICATOR_RECEIVE_FROM, args=("127.0.0.1", 12346, buffer));
rrf.start();

deltaCD = DeltaCD();
id = 0;

while(True):
    if (buffer != []):
        for counter in range(len(buffer)):
            try:
                split_item = buffer[counter].split(":");
            except:
                break;
            code = split_item[0];
            value = split_item[1];
            packet = Collection_Description(id, code, value);
            id+=1;
            send_packet = code + ":" + value;
            #add to DeltaCD
            #Check if deltaCD add and update == 10
            #Ako jeste treba da saljem readeru

            if(packet.dataset == "DATASET1"):
                print(f"DATASET1. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
                try:
                    RECEIVER_SEND_TO("127.0.0.1", 8881, send_packet, 1);
                    LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_1.\n", "127.0.0.1", 9999);
                except:
                    LOG(f"ERROR:root:[REPLICATOR RECEIVER] failed sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_1.\n", "127.0.0.1", 9999);   
            elif(packet.dataset == "DATASET2"):
                print(f"DATASET2. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
                try:
                    RECEIVER_SEND_TO("127.0.0.1", 8882, send_packet, 1);
                    LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_2.\n", "127.0.0.1", 9999);
                except:
                    LOG(f"ERROR:root:[REPLICATOR RECEIVER] failed sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_2.\n", "127.0.0.1", 9999);

            elif(packet.dataset == "DATASET3"):
                print(f"DATASET3. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
                try:
                    RECEIVER_SEND_TO("127.0.0.1", 8883, send_packet, 1);
                    LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_3.\n", "127.0.0.1", 9999);
                except:
                    LOG(f"ERROR:root:[REPLICATOR RECEIVER] failed sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_3.\n", "127.0.0.1", 9999);
            elif(packet.dataset == "DATASET4"):
                print(f"DATASET4. CODE: {packet.hc.Receiver_Property.code}, VALUE: {packet.hc.Receiver_Property.value}");
                try:
                    RECEIVER_SEND_TO("127.0.0.1", 8884, send_packet, 1);
                    LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_4.\n", "127.0.0.1", 9999);
                except:
                    LOG(f"ERROR:root:[REPLICATOR RECEIVER] failed sent {packet.hc.Receiver_Property.code}:{packet.hc.Receiver_Property.value} to Reader_4.\n", "127.0.0.1", 9999);
            else:
                print("Error...");
            buffer.pop(counter);
    else:
        pass;



#rst = threading.Thread(target=REPLICATOR_SEND_TO, args=("127.0.0.1", 11111, buffer));
#rst.start();

# REPLICATOR_RECEIVE_FROM("127.0.0.1", 12346, buffer);