# 發送指令給輪子、有條件作動
from Local_Client import WheelClient
from Local_Client import T265Client
from src import wheel_ctl_base

def messageSend(msg):

    print(f'send:{msg}'[:-1])
    WheelClient.sendToServer(sendingText=msg, ip='192.168.137.103')

def forward_Assignment(cm):

    msg = wheel_ctl_base.forward()
    messageSend(msg)
    T265Client.streamUntilDistance(ip='192.168.137.103', cm=cm)
    msg = wheel_ctl_base.stop()
    messageSend(msg)

def backward_Assignment(cm):

    msg = wheel_ctl_base.backward()
    messageSend(msg)
    T265Client.streamUntilDistance(ip='192.168.137.103', cm=cm)
    msg = wheel_ctl_base.stop()
    messageSend(msg)

def turnLeft_Assignment(degree):

    msg = wheel_ctl_base.turnLeft()
    messageSend(msg)
    T265Client.streamUntilDegree(ip='192.168.137.103', degree=degree)
    msg = wheel_ctl_base.stop()
    messageSend(msg)

def turnRight_Assignment(degree):
     
    msg = wheel_ctl_base.turnRight()
    messageSend(msg)
    T265Client.streamUntilDegree(ip='192.168.137.103', degree=degree)
    msg = wheel_ctl_base.stop()
    messageSend(msg)