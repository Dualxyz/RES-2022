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

        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            server.bind((self.host,self.port));
            server.listen();

            while True:
                client, address = server.accept();
                self.handle(client);
                client.close();
        except:
            raise TypeError("Host:Port already in use");

        

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
                        f.write(message);
            except:
                break;

if __name__ == "__main__":
    t = SERV();