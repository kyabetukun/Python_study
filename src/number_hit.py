import random
from gtts import gTTS
from pygame import mixer
import time
import cv2
# 音声出力
def say(voic):
    tts = gTTS(text=voic, lang='ja')
    tts.save("hello.mp3")
    mixer.init()
    mixer.music.load('hello.mp3')
    mixer.music.play()
#映像出力
def add(cap): 
    if not cap.isOpened():
        print("ビデオファイルを開くとエラーが発生しました")
        return

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Video", frame)
            if cv2.waitKey(30) == 27: 
                break
        else:
            break
          
#メイン機能         
print("数字を1~9で選んでください")
anther = int(input())
random_number = random.randint(1,9)

add(cv2.VideoCapture("./video/roulette.mp4"))
time.sleep(4)
print(f"ルーレットの数字は{random_number}")
time.sleep(3)

if anther == random_number:
  print('当たりです')
else:
  print("ハズレです")
cv2.destroyAllWindows()