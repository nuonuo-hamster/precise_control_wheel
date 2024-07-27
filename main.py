import threading
import KBEventHandle
from Local_Client import D435iClient

def main():

    # 錄音(R鍵)
    listener_thread = threading.Thread(target=KBEventHandle.audioListener)
    listener_thread.start()

    # 鍵盤控車
    KBAndCar_thread = threading.Thread(target=KBEventHandle.Wheels_keyboard_task)
    KBAndCar_thread.start()
    
    # D435i畫面
    D435i_thread = threading.Thread(target=D435iClient.test, args=('192.168.137.103',))
    D435i_thread.start()

if __name__ == '__main__':

    main()