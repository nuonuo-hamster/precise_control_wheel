import socket
import pickle
import math
import numpy as np

def connectServer(ip):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 8889))

    return client_socket

def getPose(client_socket):

    data = client_socket.recv(1024)
    poseArray = pickle.loads(data)
    client_socket.send("data has been received.".encode('gbk')) # 同步

    return poseArray

def streamUntilDistance(ip, cm):

    client_socket = connectServer(ip)
    
    poseArray = getPose(client_socket)
    originPosition = np.array([poseArray[1][0], poseArray[1][2]])

    while(True):

        poseArray = getPose(client_socket)
        currentPosition = np.array([poseArray[1][0], poseArray[1][2]])

        distance = 100*np.linalg.norm(currentPosition - originPosition)
        print('{:.2f} cm'.format(distance))

        if(distance >= cm): break

    client_socket.close()

def streamUntilDegree(ip, degree):

    client_socket = connectServer(ip)
    
    poseArray = getPose(client_socket)
    originDegree = poseArray[2][2]

    while(True):

        poseArray = getPose(client_socket)
        currentDegree = poseArray[2][2]

        angle = abs(currentDegree - originDegree) *180/math.pi
        print('{:.2f} degree'.format(angle))

        if(angle >= degree): break

    client_socket.close()

def test(ip):

    client_socket = connectServer(ip)
    
    for _ in range(500):
        poseArray = getPose(client_socket)
        print(poseArray)

    client_socket.close()

if __name__ == '__main__':

    test(ip='192.168.137.103')