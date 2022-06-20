import sqlite3
import datetime;
from sqlite3 import Cursor, Error
#from Reader_TCP import *;
import time;


def connect(database):
    try:
        conn = sqlite3.connect(database);
    except Error as e:
        print(e);
    return conn;


def check_if_table_exists(connection, table_name):
    sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (CODE string, VALUE string, DATETIME string);''';
    cursor = connection.cursor();
    cursor.execute(sql);
    connection.commit();

def write_to_table(connection, table_name, first, second, third):
    sql = f'''INSERT INTO {table_name}(CODE, VALUE, DATETIME) VALUES(?,?,?)''';
    cursor = connection.cursor();
    cursor.execute(sql, (first, second, third));
    connection.commit();


def read_from_table(connection, table_name):
    cursor = connection.cursor();
    cursor.execute("SELECT * FROM test");
    data = cursor.fetchall();
    packet = "CODE_ANALOG:31";
    compare_codes(connection, data,packet);

def compare_codes(connection, data, packet):
    packet = packet.split(":");
    flag = False;
    if data == []:
        flag = True;
    for i in data:
        if(packet[0] == "CODE_DIGITAL"):
            print("Code is CODE_DIGITAL. Write it to db");
            flag = True;
            break;
        else:   
            if(packet[0] == i[0]):
                #"CODE: {i[0]} Already Exists checking deadband..."
                Deadband = 0.02 * float(packet[1]);
                if(float(packet[1]) > float(i[1]) - Deadband and float(packet[1]) < float(i[1]) + Deadband):
                    print("Drop packet due to deadband diff not being greater than 2%...")
                    flag = False;
                    break;
                else:
                    #Deadband is false. Can be entered to db"
                    flag = True;
            else:
                flag = True;
                
    if(flag):                
        print(f"Packet doesn't exist. Write {packet[0]} and {packet[1]} to db...");
        table_name = "test"
        x = datetime.datetime.now();
        time = str(x.hour) + ":" + str(x.minute) + ":" + str(x.second);
        write_to_table(connection, table_name, packet[0], packet[1], time);
        #Send to logger

if __name__ == "__main__":
    database = r"D:\\User\\Desktop\\RES 2022\\RES-2022\\test.db";
    #database = r"C:\\Users\\Mateja\\Desktop\\test.db";

    #Listen for messages from Receiver
    # buffer = []
    # pravis reader_receive_from_replicator ili kako god
    # rrf = REPLICATOR_RECEIVE_FROM;
    # receive_from_thread = threading.Thread(target=rrf, args=("127.0.0.1", 12345, buffer));
    # receive_from_thread.start()

    connect = connect(database);
    table_name = "test"
    check_if_table_exists(connect, table_name);
    read_from_table(connect, table_name);
    