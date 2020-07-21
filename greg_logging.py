import os
import datetime


def write_to_log(message, error_code):

    # create the directory if it does not exist
    dir_path = '../script_logs/'
    log_path = dir_path + 'chat_server_log.txt'
    try: 
        os.makedirs(dir_path)
    except OSError:
        if not os.path.isdir(dir_path):
            raise

    # create file if it does not exist
    if not os.path.isfile(log_path):
        f=open(log_path, "a+")
        f.write('Date\tError Code\tError Message\n')
        f.close()

    # write to log file
    f=open(log_path, "a+")
    f.write(str(datetime.datetime.now()) + '\t' + str(error_code) + '\t' + message + '\n')
    f.close()

    #also print to console
    print("LOG: " + message + ", " + str(error_code))  
