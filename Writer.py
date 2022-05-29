import socket;
import threading;
import sys;
import time;

host = "127.0.0.1";
port = 12345;

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    sock.connect((host,port));
except:
    print("Could not make a connection to the server");
    sys.exit(0)

while True:
    message = input("Enter your message: ");
    #time.sleep(2);
    sock.sendall(str.encode(message));