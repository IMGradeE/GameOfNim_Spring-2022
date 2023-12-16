from time import sleep
from animalese import NotMyCode
from pydub import AudioSegment
from pydub import playback
import _thread
from pydub.playback import _play_with_pyaudio
'''
needs pydub, and ffmpeg (not sure why ffmpeg is needed but the animalese is not my code, I just modified it, and
the guy that made it says that it is needed.)
Also _thread is deprecated. Threading and Async.io are definitely better but I just wanted to bodge this together lol.
'''
def txtRndr(str,x = 1):
    NotMyCode(str,"low")
    b = AudioSegment.from_mp3('./sound.mp3')
    if str != "...":
        _thread.start_new_thread(_play_with_pyaudio,(b,))
        b = len(b)
        txtRndrLocal(str,x,b)
    else:
        txtRndrLocal(str,x)
    return ""

def txtRndrLocal(str, x = 1, b = 450):
    for i in str:
        if i == " ":
            print(i, end='')
        else:
            sleep(((b / 1000) / len(str)))
            print(i, end='')
    if x == 1:
        print('')
    else:
        print(end="")
    sleep(.2)



if __name__ == "__main__":
    str = "Hello! This program allows you to play a game of Nim against me, your computer! Have you heard of Nim before?"
    txtRndr(str)


