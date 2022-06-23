import socket;  #used for initializing the TCP connection
import sys;     #I just used it to exit but can be done without it

class LOG:
    def __init__(self, message, host, port):
        try:
            self.host = host;
            self.port = port;
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            sock.connect((self.host,self.port));
            sock.sendall(str.encode(message));

        except Exception as e:
            raise TypeError(f'''{e}. Could not make a connection to the server Host: {host}, Port {port}''');
            print(f'''{e}. Could not make a connection to the server Host: {host}, Port {port}''');
            sys.exit(0);

