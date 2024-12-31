#healthy programmeer
# water-water.mp3(3.5ltr)-dank -log-every 40 min
# eyes-eyes.mp3-eyery 30 min -eydone-log-every 30 min
# physical activity-physical.mp3 every - 45 min-exdone-log
# rules
# pygame module to play audio
from pygame import mixer
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a ==stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
    musiconloop("water.mp3","stop")

