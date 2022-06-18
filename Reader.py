import sqlite3
from sqlite3 import Cursor, Error
#from Reader_TCP import *;
import time;

#from matplotlib.pyplot import table

def connect(database):
    try:
        conn = sqlite3.connect(database);
    except Error as e:
        print(e);
    return conn;

# def create_table(connection, tuple):
def check_if_table_exists(connection, table_name):
    sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (CODE string, VALUE string);''';
    cursor = connection.cursor();
    cursor.execute(sql);
    connection.commit();

def write_to_table(connection, table_name, first, second):
    sql = f'''INSERT INTO {table_name}(CODE, VALUE) VALUES(?,?)''';
    cursor = connection.cursor();
    cursor.execute(sql, (first, second));
    connection.commit();
#Code = analog,custom, etc
#Value = random number

def read_from_table(connection, table_name,):
    cursor = connection.cursor();
    cursor.execute("SELECT * FROM test")
    data = cursor.fetchall()
    packet = "CODE_ANALOG:21"
    compare_codes(data,packet);

# 1.	CODE_ANALOG
# 2.	CODE_DIGITAL
# 3.	CODE_CUSTOM
# 4.	CODE_LIMITSET
# 5.	CODE_SINGLENOE
# 6.	CODE_MULTIPLENODE
# 7.	CODE_CONSUMER
# 8.	CODE_SOURCE

def compare_codes(data, packet):
    packet = packet.split(":");
    for i in data:
        if(packet[0] == "CODE_DIGITAL"):
            print("Code is CODE_DIGITAL")
            break;
        else:   # Ne valja odavde pa do kraja funkcije, CRINGE
            if(packet[0] == i[0] and packet[1] == str(i[1])):
                print("Already Exists...")
                break;
            else:
                Deadband = 0.02 * float(packet[1])
                if(float(packet[1]) < float(i[1]) - Deadband  and float(packet[1]) > float(i[1]) + Deadband):
                    print("Do nothing...")
                    break;
                else:
                    print("Write to DB...")
                


if __name__ == "__main__":
    database = r"C:\\Users\\Mateja\\Desktop\\test.db";
    connect = connect(database);
    table_name = "test"
    check_if_table_exists(connect, table_name);
    # write_to_table(connect, table_name, "CODE_ANALOG", "45");
    # write_to_table(connect, table_name, "CODE_SINGLENODE", "31");
    # write_to_table(connect, table_name, "CODE_DIGITAL", "12");
    # write_to_table(connect, table_name, "CODE_ANALOG", "21");
    # write_to_table(connect, table_name, "CODE_SINGLENODE", "31");
    # write_to_table(connect, table_name, "CODE_DIGITAL", "67");
    read_from_table(connect, table_name);
    