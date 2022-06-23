from READER_RECEIVE_CLASS import READER_RECEIVE
from SEND_TO_LOG import LOG;
from READER_OOP import READER_TO_DB;
import threading;


if __name__ == "__main__":
    LOG("INFO:root:[REPLICATOR SENDER] has started.\n", "127.0.0.1", 9999);

    buffer = [];

    rrc = READER_RECEIVE;
    rtdb = READER_TO_DB;

    rrc_thread = threading.Thread(target=rrc, args=("127.0.0.1", 8881, buffer, 1));
    rtdb_thread = threading.Thread(target=rtdb, args=(buffer,));

    rrc_thread.start();
    rtdb_thread.start();

    