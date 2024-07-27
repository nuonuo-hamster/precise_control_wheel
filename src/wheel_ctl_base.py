def stop():

    data_to_send = f'0 80 80 80 80\n'
    return data_to_send

def forward():

    data_to_send = f'1 80 80 80 80\n'
    return data_to_send

def backward():

    data_to_send = f'2 80 80 80 80\n'
    return data_to_send

def turnLeft():

    data_to_send = f'8 80 80 80 80\n'
    return data_to_send

def turnRight():

    data_to_send = f'9 80 80 80 80\n'
    return data_to_send

def shiftLeft():

    data_to_send = f'3 80 80 80 80\n'
    return data_to_send

def shiftRight():

    data_to_send = f'4 80 80 80 80\n'
    return data_to_send

def main():
    pass

if __name__ == '__main__':

    main()