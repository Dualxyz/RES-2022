import sqlite3
import datetime;
from sqlite3 import Cursor, Error
#from Reader_TCP import *;
import time;

from SEND_TO_LOG import LOG;


class READER_TO_DB:
    def __init__(self, buffer):
        try:
            while(True):
                if(buffer !=[]):
                    print(str(buffer));
                    packet = buffer[0];
                    self.database = r"D:\\User\\Desktop\\RES 2022\\RES-2022\\test.db";
                    self.connectvar = self.connect(self.database);
                    self.table_name = "test"
                    self.check_if_table_exists(self.connectvar, self.table_name);
                    self.read_from_table(self.connectvar, self.table_name, packet);
                    buffer.pop(0);
                else:
                    pass;
        except:
            pass;


    def connect(self, database):
        try:
            conn = sqlite3.connect(database);
            LOG("INFO:root:[READER] has successfully connected to db.\n", "127.0.0.1", 9999);
            return conn;
        except Error as e:
            print(e);
            return -1;


    def check_if_table_exists(self, connection, table_name):
        try:
            sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (CODE string, VALUE string, DATETIME string);''';
            cursor = connection.cursor();
            cursor.execute(sql);
            connection.commit();
            return 0;
        except:
            return -1;

    def write_to_table(self, connection, table_name, first, second, third):
        sql = f'''INSERT INTO {table_name}(CODE, VALUE, DATETIME) VALUES(?,?,?)''';
        cursor = connection.cursor();
        cursor.execute(sql, (first, second, third));
        connection.commit();

    def read_from_table(self, connection, table_name, buffer):
        cursor = connection.cursor();
        cursor.execute("SELECT * FROM test");
        data = cursor.fetchall();
        packet = "CODE_ANALOG:11";
        #self.compare_codes(connection, data,packet);
        self.compare_codes(connection, data,buffer);

    def compare_codes(self,connection, data, packet):
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
                        LOG(f"WARNING:root:[READER] deadband exception for {packet[0]}:{packet[1]}.\n", "127.0.0.1", 9999);
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
            self.write_to_table(connection, table_name, packet[0], packet[1], time);
            LOG(f"INFO:root:[READER] wrote {packet[0]}:{packet[1]} at {time} to db.\n", "127.0.0.1", 9999);
