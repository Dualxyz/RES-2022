import socket;  #used for initializing the TCP connection
import sys;     #I just used it to exit but can be done without it
import time;    #self-explanatory
import random;  #self-explanatory
from CODE_LIST import CODE_LIST;    #Imports the list of codes that we have to send to the Replicator_Sender

from SEND_TO_LOG import LOG;

class Writer:
    """
    send_message(self->Instance of the class, sock-> socket on which it's connected)
    CODE_LIST contains the list of codes
    random.randint(from 0, to length of the list - 1) + "splitter ':'" + random value in range 1-100
    str.encode encode the bytes so that they can be sent through the socket(socket.sendall)
    """
    def send_message(self,sock):
        while(True):
            code = CODE_LIST[random.randint(0, len(CODE_LIST)-1)];
            value = str(random.randint(1,100));
            sock.sendall(str.encode(code + ":" + value));

            logging_info = f"INFO:root:[WRITER] Writer sent a {code}:{value} to ReplicatorSender.\n";
            LOG(logging_info);

            time.sleep(2);

    """
    Creates a TCP(SOCK_STREAM) socket with IPv4 connection (AF_INET)
    """
    def __init__(self):
        host = "127.0.0.1";
        port = 12345;

        try:
            logging_info = "INFO:root:[WRITTER] Successfully connected to ReplicatorSender\n";
            LOG(logging_info);

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            sock.connect((host,port));
            self.send_message(sock);

        except Exception as e:
            #print(f'''{e}. Could not make a connection to the server Host: {host}, Port {port}''');
            logging_error = f"[WRITER] FAILED TO CONNECT. REPLICATOR SENDER IS DOWN.\n";
            LOG(logging_error);
            #sys.exit(0);
