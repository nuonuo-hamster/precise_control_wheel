#處理voiceRecognize的字串，交給wheelsHandle作動
import re
import wheelsHandle

forward_list = ['前進', '田徑']
backward_list = ['後退']
turnLeft_list = ['左轉']
turnRight_list = ['右轉']

cm_list = ['公分']
degree_list = ['度']

functionType, value = None, None

def sentenceAnalysis(text):

    global functionType, value

    # 前進
    match_head = [word for word in forward_list if word in text]
    if len(match_head) == 1:
        # 公分
        match_tail = [word for word in cm_list if word in text]
        if len(match_tail) == 1:
            # 先後順序
            if(text.index(match_head[-1]) < text.index(match_tail[0])):
                value_match = re.search(f'(\d+)\s*{match_tail[0]}', text)
                # 數值
                if value_match:
                    functionType = 'forward'
                    value = value_match.group(1)
        return
    
    # 後退
    match_head = [word for word in backward_list if word in text]
    if len(match_head) == 1:
        # 公分
        match_tail = [word for word in cm_list if word in text]
        if len(match_tail) == 1:
            # 先後順序
            if(text.index(match_head[-1]) < text.index(match_tail[0])):
                value_match = re.search(f'(\d+)\s*{match_tail[0]}', text)
                # 數值
                if value_match:
                    functionType = 'backword'
                    value = value_match.group(1)
        return
    
    # 左轉
    match_head = [word for word in turnLeft_list if word in text]
    if len(match_head) == 1:
        # 度
        match_tail = [word for word in degree_list if word in text]
        if len(match_tail) == 1:
            # 先後順序
            if(text.index(match_head[-1]) < text.index(match_tail[0])):
                value_match = re.search(f'(\d+)\s*{match_tail[0]}', text)
                # 數值
                if value_match:
                    functionType = 'turnLeft'
                    value = value_match.group(1)
        return
    
    # 右轉
    match_head = [word for word in turnRight_list if word in text]
    if len(match_head) == 1:
        # 度
        match_tail = [word for word in degree_list if word in text]
        if len(match_tail) == 1:
            # 先後順序
            if(text.index(match_head[-1]) < text.index(match_tail[0])):
                value_match = re.search(f'(\d+)\s*{match_tail[0]}', text)
                # 數值
                if value_match:
                    functionType = 'turnRight'
                    value = value_match.group(1)
        return

def instrunctionExcute():

    global functionType, value
    value = int(value)
    print(f'type: {functionType}, value: {value}')

    if(functionType != None and value != None):

        if (functionType == 'forward'):
            wheelsHandle.forward_Assignment(cm=value)

        elif (functionType == 'backward'):
            wheelsHandle.backward_Assignment(cm=value)

        elif (functionType == 'turnLeft'):
            wheelsHandle.turnLeft_Assignment(degree=value)

        elif (functionType == 'turnRight'):
            wheelsHandle.turnRight_Assignment(degree=value)

        functionType, value =  None, None
    else:
        print("no instruction assigned.(value invalid)")

def test():

    sentenceAnalysis('前進 20公分')
    # sentenceAnalysis('後退 10公分')
    # sentenceAnalysis('左轉 20度')
    # sentenceAnalysis('右轉 30度')

    instrunctionExcute()

if __name__ == '__main__':

    test()