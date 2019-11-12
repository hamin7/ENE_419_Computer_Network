import socket
import maya.cmds as cmds

def startrealtimeexp(*args):
    global recstart

    if True >= 0:
        if recstart == 0:
            recstart = 1
            cmds.button( 'realtimecomm' ,edit=True, label = 'Stop Real Time Expression' )
	    #Start Comm
            cmds.commandPort(name="127.0.0.1:7777", echoOutput=False, noreturn=False,prefix="portData", returnNumCommands=True)
            cmds.commandPort(name=":7777", echoOutput=False, noreturn=False,prefix="portData", returnNumCommands=True)
        else:
            recstart = 0
            cmds.button( 'realtimecomm' ,edit=True, label = 'Start Real Time Expression' )
	    #Stop Comm
            deactivateCommandPort('127.0.0.1', '7777')

def deactivateCommandPort(host, port):
    path = host + ":" + port
    active = cmds.commandPort(path, q=True)
    if active:
        cmds.commandPort(name=path, cl=True)
    else:
        print("%s is was not active" % path)