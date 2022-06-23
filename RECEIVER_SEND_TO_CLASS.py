import socket;  #used for initializing the TCP connection
import sys;     #I just used it to exit but can be done without it
import time;    #self-explanatory
import random;  #self-explanatory
from CODE_LIST import CODE_LIST;    #Imports the list of codes that we have to send to the Replicator_Sender


from SEND_TO_LOG import LOG;

class RECEIVER_SEND_TO:
    """
    Creates a TCP(SOCK_STREAM) socket with IPv4 connection (AF_INET)
    """
    def __init__(self, host, port, message, instance):
        self.instance = instance;

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            sock.connect((host,port));
            sock.sendall(str.encode(message));
            logging_info = f"INFO:root:[REPLICATOR RECEIVER] send {message} to READER_{self.instance}.\n"
            LOG(logging_info, "127.0.0.1", 9999);
            sock.close();

        except Exception as e:
            #print(f'''{e}. Could not make a connection to the server Host: {host}, Port {port}''');
            logging_error = "ERROR:root:[REPLICATOR SENDER] FAILED TO CONNECT. REPLICATOR RECEIVER IS DOWN.\n";
            LOG(logging_error, "127.0.0.1", 9999);
            sys.exit(0);

if __name__ == "__main__":
    RECEIVER_SEND_TO("127.0.0.1", 8881, "nekicode:nekivalue", 1);
