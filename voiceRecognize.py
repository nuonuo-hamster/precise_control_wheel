# 錄音、辨識，並交由sentenseHandle
import speech_recognition as sr
import sentenseHandle

# status
is_recording = False
audio_data = None

r = sr.Recognizer()

def startRecording():
    global is_recording, audio_data

    if not is_recording:
        is_recording = True
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("recording...")
            audio_data = r.listen(source)
        print("record completed")

def audioProcess():
    global is_recording, audio_data

    if  is_recording:
        is_recording = False
        if audio_data is not None:
            try:
                print("try to rcognize...")
                text = r.recognize_google(audio_data, language='zh-TW', show_all=False)
                print(f"result：{text}")
                sentenseHandle.sentenceAnalysis(text)
                sentenseHandle.instrunctionExcute()

            except sr.UnknownValueError:
                print("cannot recognize...")
            except sr.RequestError as e:
                print(f"request err：{e}")
            audio_data = None  # reset audio_data 
        else:
            print("theres no audio data")