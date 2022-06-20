import multiprocessing
import os
import socket
import threading
import time

from SEND_TO_LOG import LOG;
import logging;
from io import StringIO;

#from numpy import append
#SOURCE : https://gist.github.com/micktwomey/606178

class REPLICATOR_RECEIVE_FROM:
    def __init__(self, host, port, buffer):
        self.host = host;
        self.port = port;
        self.buffer = buffer;

        log_stream = StringIO();
        logging.basicConfig(stream=log_stream, level=logging.INFO);

        log_stream.truncate(0);
        logging.info(f"[REPLICATOR SENDER] Started a server on {self.host}:{self.port}.");
        LOG(log_stream.getvalue().strip("\x00")); #?????????????????????????????????????????????????
        log_stream.truncate(0);

        print(f"Started a server on {self.host}:{self.port}.\n");

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        server.bind((self.host,self.port));
        server.listen();

        while True:
            client, address = server.accept()
            print(f"Connected with {str(address)}.");

            t = threading.Thread(target=self.handle, args=(client,buffer, log_stream));
            t.start();

    def handle(self, client, buffer, log_stream):
        while True:
            try:
                message = client.recv(1024).decode('ascii');
                if message == '':
                    client.close();
                else:
                    try:
                        print(f"Client RADDR: {client.raddr}");
                    except:
                        pass;

                    logging.info(f"[REPLICATOR SENDER] Received a message: {message}.");
                    LOG(log_stream.getvalue().strip("\x00")); #?????????????????????????????????????????????????
                    log_stream.truncate(0);
                    print(f"Message: {message}");
                    buffer.append(message);
            except:
                break;
