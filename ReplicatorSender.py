from concurrent.futures import thread
from SENDER_RECEIVE_FROM_CLASS import REPLICATOR_RECEIVE_FROM;
from SENDER_SEND_TO_CLASS import REPLICATOR_SEND_TO;
import threading;
import time;
import os;
from SEND_TO_LOG import LOG;

if __name__ == "__main__":
    with open("pid.txt", 'w') as f:
        f.write(str(os.getpid()));

    LOG("INFO:root:[REPLICATOR SENDER] has started.\n");

    buffer = [];


    rrf = REPLICATOR_RECEIVE_FROM;
    rst = REPLICATOR_SEND_TO;

    receive_from_thread = threading.Thread(target=rrf, args=("127.0.0.1", 12345, buffer));
    send_to_thread = threading.Thread(target=rst, args=("127.0.0.1", 12346, buffer));
    receive_from_thread.start();
    send_to_thread.start();
    
