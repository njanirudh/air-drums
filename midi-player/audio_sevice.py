from audio_player import WavPlayer
from enum import Enum

class Tune(Enum):
    HiHatOpen =1
    HiHatClose = 2
    Snare = 3
    BassDrum = 4
    Crash = 5
    Ride = 6
    TomsSmall = 7
    TomsLarge = 8
    TomsFloor = 9

class AudioService:

    def __init__(self):
        self.HiHatOpenPlayer  = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.HiHatOpenPlayer.start()

        self.HiHatClosePlayer = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.HiHatClosePlayer.start()

        self.SnarePlayer      = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.SnarePlayer.start()

        self.BassDrumPlayer   = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.BassDrumPlayer.start()

        self.CrashPlayer      = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.CrashPlayer.start()

        self.RidePlayer       = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.RidePlayer.start()

        self.TomsSmallPlayer  = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.TomsSmallPlayer.start()

        self.TomsLargePlayer  = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.TomsLargePlayer.start()

        self.TomsFloorPlayer  = WavPlayer("/home/anirudh/Music/MiDi/Closed-Hi-Hat-1.wav")
        self.TomsFloorPlayer.start()

    def run_audio(self, tune_type:Tune):
        if tune_type == Tune.HiHatOpen:
            self.HiHatOpenPlayer.play()

        if tune_type == Tune.HiHatClose:
            self.HiHatClosePlayer.play()

        if tune_type == Tune.Snare:
            self.SnarePlayer.play()

        if tune_type == Tune.BassDrum:
            self.BassDrumPlayer.play()

        if tune_type == Tune.Crash:
            self.CrashPlayer.play()

        if tune_type == Tune.Ride:
            self.RidePlayer.play()

        if tune_type == Tune.TomsSmall:
            self.TomsSmallPlayer.play()

        if tune_type == Tune.TomsLarge:
            self.TomsLargePlayer.play()

        if tune_type == Tune.TomsFloor:
            self.TomsFloorPlayer.play()






