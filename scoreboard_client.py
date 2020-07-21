import socket
import datetime
import os
import json
import errno
import sys

from bibliopixel.layout import *
from scoreboard.animations.ScoreBoardUpdateAnimation import ScoreBoardUpdateAnimation # import the animation
from bibliopixel.drivers.PiWS281X import *

from greg_logging import write_to_log

"""
#create biblio pixel driver and led
thread     = False   # display updates to run in background thread
brightness = 100     # brightness 0-255
driver     = PiWS281X(325)
led        = Strip(driver, thread, brightness)
"""

SERVER_IP="10.0.0.180"
SERVER_PORT=9010
RECV_BUFF_SIZE=4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#anim  = ScoreBoardUpdateAnimation(led, 1200, .05) 

realHomeName = "home"
realAwayName = "away"

def init_client():
    # first establish connection to server
    sock.settimeout(1)
    sock.setblocking(0)

    try:
        sock.connect((SERVER_IP, SERVER_PORT))
    except socket.error as e:
        err = e.args[0]
        if err != errno.EINPROGRESS:
            write_to_log("Unable to connect " + str(sys.exc_info()), 3)
            print(sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR))
            sys.exit(1)
     
    sock_error = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
    while sock_error:
        print(sock_error)
     
    write_to_log('Connected to remote host.', 0)
    #sys.stdout.flush()

    
def get_commands():
    """
    anim.homeName = "ini1"
    anim.awayHome = "ini2"
    anim.homeScore = 69
    anim.awayscore = 69
    start_anim()
    """

    while 1:
        """        
        if anim.isDone:
            anim = ScoreBoardUpdateAnimation(led, 86400, .05)
            anim.homeName = realHomeName
            anim.awayName = realAwayName
            start_anim() 
        """

        # get scoreboard commands if there are some
        try:
            data = sock.recv(RECV_BUFF_SIZE)
        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                continue
            else:
                # a "real" error occurred
                print(e)
                sys.exit(1)
        else:
            # got a message, do something :)
            if not data:
                write_to_log('Disconnected from chat server', 1)
                sock.close()
                sys.exit()
            print(str(data))
            json_data = json.loads(data.decode("utf-8"))
            print(json_data)
            command = json_data[0]
            commandType = command["command"]
            commandParams = command["parameters"]
            handle_commands(str(commandType), commandParams)
            #myCommand = json_data[0]
            #run animation

def handle_commands(command, params): 
    if command == "updateScoreboard":
        print(params["awayScore"])
        print(params["homeScore"])
        """
        anim.homeScore = int(params["homeScore"])
        anim.awayScore = int(params["awayScore"])
        """
    elif command == "resetScoreboard": #reset
        """
        if anim.isRunning:
            anim.stop()
            anim.isDone.wait()
        """
        realHomeName = str(params["homeName"])
        realAwayName = str(params["awayName"])
        utcStr = str(params["end"])
        startTime = datetime.datetime.now()
        endTime = datetime.datetime.strptime(utcStr, "%Y-%m-%d %H:%M:%S")
        deltaTime = endTime - startTime
        print(deltaTime.total_seconds())
        """
        anim = ScoreBoardUpdateAnimation(led, deltaAnim.total_seconds(), .05)
        start_anim()
        """

"""
def start_anim():
    animThread = threading.Thread(target=anim.run)
    animThread.start()
    animThread.isDone.clear()
"""

if __name__ == "__main__":
    init_client()
    sys.exit(get_commands())