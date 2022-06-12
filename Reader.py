import sqlite3
from sqlite3 import Error
from Reader_TCP import *;
import time;

from matplotlib.pyplot import table

def connect(database):
    try:
        conn = sqlite3.connect(database);
    except Error as e:
        print(e);
    return conn;

# def create_table(connection, tuple):
def check_if_table_exists(connection, table_name):
    sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (DATA_SET string, CODE string);''';
    cursor = connection.cursor();
    cursor.execute(sql);
    connection.commit();

def write_to_table(connection, table_name, first, second):
    sql = f'''INSERT INTO {table_name}(DATA_SET, CODE) VALUES(?,?)''';
    cursor = connection.cursor();
    cursor.execute(sql, (first, second));
    connection.commit();

if __name__ == "__main__":
    database = r"D:\\User\\Desktop\\RES 2022\\Hai\\MOJ_RES_PROJEKAT\\test1.db";
    connect = connect(database);
    table_name = "test1"
    check_if_table_exists(connect, table_name);
    write_to_table(connect, table_name, "DATA_SET 1", "CODE_ANALOG");
    write_to_table(connect, table_name, "DATA_SET 2", "CODE_CUSTOM");
    write_to_table(connect, table_name, "DATA_SET 3", "CODE_SINGLENODE");