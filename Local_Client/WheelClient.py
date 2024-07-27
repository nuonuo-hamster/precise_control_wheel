import socket

def connectWheelServer(ip):
  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 8899))
    return client_socket

def sendText(client_socket, text):
    client_socket.send(text.encode())

def clientClose(client_socket):
    client_socket.close()

def sendToServer(sendingText, ip):

    try:
        client_socket = connectWheelServer(ip)
        
        try:
            sendText(client_socket, text=sendingText)
            print('send access.')
        except:
            print('failed to send.')

        clientClose(client_socket)
    except:
        print("failed to send.")

def test(ip):
    
    try:
        print("connect Wheel server...")
        client_socket = connectWheelServer(ip)
        print("connect success.")
        
        try:
            sendText(client_socket, text='0 70 70 70 70\n')
        except:
            print('send text failed.')

        clientClose(client_socket)
    except:
        print("connect err.")

if __name__ == '__main__':

    test(ip='192.168.137.103')

    

    
