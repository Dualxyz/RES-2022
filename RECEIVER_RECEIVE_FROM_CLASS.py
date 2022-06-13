import socket
import threading

class REPLICATOR_RECEIVE_FROM:
    def __init__(self, host, port, buffer):
        self.host = host;
        self.port = port;
        self.buffer = buffer;
        print(f"Started a server on {self.host}:{self.port}.\n");

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        server.bind((self.host,self.port));
        server.listen();

        while True:
            client, address = server.accept()
            print(f"Connected with {str(address)}.");

            t = threading.Thread(target=self.handle, args=(client,buffer));
            t.start();

    def handle(self, client, buffer):
        while True:
            try:
                message = client.recv(1024).decode('ascii');
                if message == '':
                    client.close();
                else:
                    #print(f"Message: {message}");
                    buffer.append(message);
            except:
                break;
