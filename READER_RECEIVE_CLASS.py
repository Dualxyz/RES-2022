import socket
import threading

from SEND_TO_LOG import LOG;

class READER_RECEIVE:
    def __init__(self, host, port, buffer, instance):
        self.host = host;
        self.port = port;
        self.buffer = buffer;
        self.instance = instance;

        logging_info = (f"INFO:root:[READER_{str(self.instance)}] Started a server on {self.host}:{self.port}.\n");
        LOG(logging_info);

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
                    pass;

                    logging_info = (f"INFO:root:[READER_{str(self.instance)}] Received a message from: {message}.\n");
                    LOG(logging_info);
                    print(f"Message: {message}");
                    buffer.append(message);
            except:
                break;
