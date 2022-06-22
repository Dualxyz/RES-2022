import sys
from WRITER_CLASS import Writer;    #Import the Writer class
import multiprocessing;
import subprocess;  #used for executing system commands (powershell/cmd)
from SEND_TO_LOG import LOG;
from io import StringIO;




def list_process(process_dictionary):
    try:
        for item in process_dictionary:
            print(f"{item} : {process_dictionary[item]}");
        return 0;  
    except:
        return -1;

def delete_all_writers(process_dictionary):
    try:
        for item in process_dictionary:
            try:
                subprocess.run(f"taskkill /F /PID {process_dictionary[item]}", stderr=subprocess.STDOUT);
                logging_info = f"WARNING:root:[WRITER] Writer {process_dictionary[item]} successfully closed.\n";
                LOG(logging_info);
            except:
                print(f"Process with an id: {process_dictionary[item]} doesn't exist");
        return 0;
    except:
        return -1;


def Menu():
    process_dictionary = {};    #Dictionary to store Writer instance + ProcessID
    instance_counter = 0;       #Writer instance
    while(True):
        print(15 * "-" + "MENU" + 15 * "-");
        print("1. Create writer.");
        print("2. Destroy writer.");
        print("3. Exit ");
        option = input("Your option: ");

        if option == "1":
            p = multiprocessing.Process(target=Writer);
            p.start();
            process_dictionary[instance_counter] = p.pid;
            logging_info = f"INFO:root:[WRITER] Successfully started a {instance_counter}. writer.\n";
            LOG(logging_info);
            instance_counter+=1;
            
        elif option == "2":
            if process_dictionary != {}:
                list_process(process_dictionary);
                option1 = int(input("Enter the instance: "));
                try:
                    subprocess.run(f"taskkill /F /PID {process_dictionary[option1]}", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT);
                    print(f"Writer {option1} successfully closed.");

                    logging_info = f"WARNING:root:[WRITER] Writer {option1} successfully closed.\n";
                    LOG(logging_info);

                    process_dictionary.pop(option1);
                except:
                    print("Wrong Instance number");
                for item in process_dictionary:
                    print(f"ID: {item} -> ProcessID: {process_dictionary[item]}");
            else:
                print("No writers were started.");

        elif option == "3":
            print("Exiting...");
            delete_all_writers(process_dictionary);
            sys.exit();
        else:
            print("Wrong option try again.")

if __name__ == "__main__":
    Menu();
