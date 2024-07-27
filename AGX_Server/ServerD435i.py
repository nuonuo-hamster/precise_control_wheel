import cv2
import socket
import pickle
import struct

from .cam import d435i

def connectD435i(width=640, height=480):

    pipe = d435i.realsense_init(width=640, height=480)
    return pipe

def serverOpen():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    return server_socket

def loopSendFrame(tunnel, pipe):
    
    connection = tunnel.makefile('wb')

    while (True):
        
        depth_frame, color_image, depth_cm = d435i.realsense_run(pipe)
        data = pickle.dumps(color_image)
        size = struct.pack('!I', len(data))
        connection.write(size)
        connection.write(data)
        
        if cv2.waitKey(1) == 27: # esc
            break

    connection.close()

def main():

    print("connect D435i...")
    pipe = connectD435i(width=640, height=480)

    print("open server...")
    server_socket = serverOpen()

    while(True):
        try:
            print("Wait for client...")
            tunnel, addr = server_socket.accept()
            
            print("send frame...")
            loopSendFrame(tunnel, pipe)
            
            tunnel.close()
            print("client offline")
        except:
            print("Server Err")
            
    pipe.stop()

if __name__ == '__main__':

    main()