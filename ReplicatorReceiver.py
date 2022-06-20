import threading
from RECEIVER_RECEIVE_FROM_CLASS import REPLICATOR_RECEIVE_FROM;
from SENDER_SEND_TO_CLASS import REPLICATOR_SEND_TO;
import threading;
from DeltaCD import DeltaCD;
from SEND_TO_LOG import LOG;

LOG("INFO:root:[REPLICATOR RECEIVER] has started.\n");

buffer=[];
rrf = threading.Thread(target=REPLICATOR_RECEIVE_FROM, args=("127.0.0.1", 12346, buffer));
rrf.start();

deltaCD = DeltaCD();

while(True):
    if (buffer != []):
        for counter in range(len(buffer)):
            split_item = buffer[counter].split(":");
            code = split_item[0];
            value = split_item[1];


            #add to DeltaCD
            #Check if deltaCD add and update == 10
            #Ako jeste treba da saljem readeru

            if(code == "CODE_ANALOG" or code == "CODE_DIGITAL"):
                print(f"DATASET1. CODE: {code}, VALUE: {value}");
                LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {code}:{value} to Reader_1.\n");
            elif (code == "CODE_CUSTOM" or code == "CODE_LIMITSET"):
                print(f"DATASET2. CODE: {code}, VALUE: {value}");
                LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {code}:{value} to Reader_2.\n");
            elif (code == "CODE_SINGLENODE" or code == "CODE_MULTIPLENODE"):
                print(f"DATASET3. CODE: {code}, VALUE: {value}");
                LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {code}:{value} to Reader_3.\n");
            elif (code == "CODE_CONSUMER" or code == "CODE_SOURCE"):
                print(f"DATASET4. CODE: {code}, VALUE: {value}");
                LOG(f"INFO:root:[REPLICATOR RECEIVER] sent {code}:{value} to Reader_4.\n");
            buffer.pop(counter);
    else:
        pass;



#rst = threading.Thread(target=REPLICATOR_SEND_TO, args=("127.0.0.1", 11111, buffer));
#rst.start();

# REPLICATOR_RECEIVE_FROM("127.0.0.1", 12346, buffer);