import simpleaudio as sa
import threading
import time

class WavPlayer(threading.Thread) :

    def __init__(self,path):
        super().__init__()
        self.wav_obj = sa.WaveObject.from_wave_file(path)

    def play(self):
        self.play_object = self.wav_obj.play()

    def stop(self):
        self.play_object.stop()

    def run(self):
        return


if __name__ == "__main__":

    path_1 = '/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav'

    closed_hi_hat = WavPlayer(path_1)
    closed_hi_hat.start()

    closed_hi_hat.play()
    time.sleep(5)
    closed_hi_hat.play()