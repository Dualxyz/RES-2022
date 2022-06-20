import datetime
import multiprocessing
import os
import socket
import threading
import time

class SERV:
    def __init__(self):
        self.host = "127.0.0.1";
        self.port = 9999;
        print(f"Logger on {self.host}:{self.port}.\n");

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        server.bind((self.host,self.port));
        server.listen();

        while True:
            client, address = server.accept();
            self.handle(client);
            client.close();

    def handle(self, client):
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
                    print(f"{message}");
                    with open("log.txt", "a") as f:
                        # x = datetime.datetime.now();
                        # time = str(x.hour) + ":" + str(x.minute) + ":" + str(x.second);
                        #print((message));
                        f.write(message);
                        #print(time + str(message));
            except:
                break;

if __name__ == "__main__":
    t = SERV();