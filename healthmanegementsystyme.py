import pygame
import datetime
import time
print("Welcome to the program.We care for your Health")
try:
    f=open("mylogs.txt","x")
    f.close()
except Exception as e:
    print(end=" ")
Water_interval=2400
Exercise_interval=45*60
Eyes_interval=1800
def musiconloop(file,music,stopper,statement):
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    print(f"please enter\"{stopper}\"to stop")
    a=input()
    if a==stopper:
        pygame.mixer_music.stop()
        f = open("mylogs.txt", "a")
        f.write(f"{statement} {datetime.datetime.today()}")
        f.close()
initial_time=time.time()
while True:
    if time.time()-initial_time>Water_interval:
        Water_interval = Water_interval + 2400
        musiconloop("mylogs.txt","song.mp3","Drank","Water drank on")
    if time.time()-initial_time>Eyes_interval:
        Eyes_interval = Eyes_interval+45*60
        musiconloop("mylogs.txt","song.mp3",'Done',"Eyes  exercise done on")
    if time.time()-initial_time>Exercise_interval:
        Exercise_interval=Exercise_interval+1800

        musiconloop("mylogs.txt","song.mp3","Done","Exercise done on")
