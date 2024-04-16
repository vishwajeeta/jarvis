from vosk import Model,KaldiRecognizer
import pyaudio
import os
#path of vosk english-hindi
model=Model("./vosk/vosk-model-small-en-in-0.4")
recognizer= KaldiRecognizer(model,16000)

mic=pyaudio.PyAudio()
stream=mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
    data=stream.read(4096)
    if len(data)==0:
        print("not working")
        break
    if recognizer.AcceptWaveform(data):
        UserSaid=recognizer.Result()[14:-3]
        print(UserSaid)
        if UserSaid =='start chrome':
            os.system("start chrome")
        elif UserSaid =='exit':
            break
        
        