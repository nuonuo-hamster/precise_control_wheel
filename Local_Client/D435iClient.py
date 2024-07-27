import cv2
import time
import socket
import pickle
import struct

def connectServer(ip):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 8888))

    return client_socket

def GetFrame(tunnel):
    
    size = struct.unpack('!I', tunnel.read(struct.calcsize('!I')))[0]
    data = tunnel.read(size)
    frame = pickle.loads(data)

    return frame

def clientClose(client_socket):
    client_socket.close()

def test(ip='192.168.137.103'):
    
    try:
        print("connect server...")
        client_socket = connectServer(ip)
        print("connect success.")

        try:
            print("Getting Frame...")
            tunnel = client_socket.makefile('rb')

            while True:

                frame = GetFrame(tunnel)
                
                cv2.imshow('Client', frame)
                if cv2.waitKey(1) == 27: # esc
                    break
            cv2.destroyAllWindows()

            tunnel.close()
        except:
            print("Get D435i Frame Err.")

        clientClose(client_socket)
    except:
        print("connect err.")

if __name__ == '__main__':
    
    test(ip='192.168.137.103')