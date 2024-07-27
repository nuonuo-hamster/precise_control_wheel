import socket
import time
import serial

def connectArduino(port='/dev/ttyACM0', rate=9600):

    ser = serial.Serial(port, rate)
    time.sleep(1)
    return ser

def sent_massege(ser, text):

    data_to_send = text
    ser.write(data_to_send.encode()) 

def serverOpen():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8899))
    server_socket.listen(5)
    return server_socket

def decodeAndSend(tunnel, ser):
    
    data = tunnel.recv(1024).decode()
    if data:
        print(f"Received data: {data}")
        sent_massege(ser, text= data)

def main():

    print("connect arduino...")
    try:
        ser = connectArduino(port='/dev/ttyACM0', rate=9600)
    except:
        try:
            ser = connectArduino(port='/dev/ttyACM1', rate=9600)
        except:
            print("arduino connect err.")
            return

    print("open Server...")
    server_socket = serverOpen()

    while(True):
        try:
            print("Wait for client...")
            tunnel, addr = server_socket.accept()
            
            try:
                print("send message...")
                decodeAndSend(tunnel, ser)
            except:
                print("wheels send error.")

            tunnel.close()
            print("client offline.")
        except:
            print("Server Err")
            break

if __name__ == '__main__':

    main()
