import socket;
import threading;
import os;

host = "127.0.0.1";
port = 12345;
temp_buffer = [];

print(f"Started a server on {host}:{port}.\n");

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server.bind((host,port));
server.listen();

def add_to_buffer(message):
    temp_buffer.append(message);

def handle(client, address):
    while True:
        try:
            message = client.recv(1024).decode('ascii');
            
            if message == '':
                client.close();
            else:
                print(f"Client: {client}");
                try:
                    print(f"Client RADDR: {client.raddr}");
                except:
                    pass;
                print(f"Addr: {address}");
                print(f"Message: {message}");
        except:
            break;


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}.");

        thread = threading.Thread(target=handle, args=(client,address,));
        thread.start();

if __name__ == "__main__":
    with open("pid.txt", 'w') as f:
        f.write(str(os.getpid()));

    receive();

