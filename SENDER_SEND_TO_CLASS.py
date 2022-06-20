import socket;  #used for initializing the TCP connection
import sys;     #I just used it to exit but can be done without it
import time;    #self-explanatory
import random;  #self-explanatory
from CODE_LIST import CODE_LIST;    #Imports the list of codes that we have to send to the Replicator_Sender


from SEND_TO_LOG import LOG;
import logging;
from io import StringIO;

class REPLICATOR_SEND_TO:
    """
    Creates a TCP(SOCK_STREAM) socket with IPv4 connection (AF_INET)
    """
    def __init__(self, host, port, buffer):
        log_stream = StringIO();
        logging.basicConfig(stream=log_stream, level=logging.INFO);
        log_stream.truncate(0);

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            sock.connect((host,port));
            while(True):
                if(buffer != []):
                    message = buffer[0];
                    sock.sendall(str.encode(message));
                    logging.info(f"[WRITER] Writer sent a something to ReplicatorSender.");
                    logging_info = f"INFO:root:[REPLICATOR SENDER] send {message} to Replicator Receiver.\n"
                    log_stream.truncate(0);
                    LOG(logging_info);
                    buffer.pop(0);
                else:
                    pass;

        except Exception as e:
            print(f'''{e}. Could not make a connection to the server Host: {host}, Port {port}''');
            sys.exit(0);
