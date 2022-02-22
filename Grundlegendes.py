#Grundlegendes

#Importierung aller nötigen Pakete
import pygame, os, sys, random

def path(path): # PyInstaller
    base_path = getattr(sys,"_MEIPASS",os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path,path)

#Pygame wird initalisiert
pygame.init()

#Schrift
schrift1 = pygame.font.Font(path("zusatz/Oswald-Bold.ttf"),32)
schrift2 = pygame.font.Font(path("zusatz/Oswald-Medium.ttf"),25)
#https://www.fontsquirrel.com/fonts/download/oswald

#Icon für das Spiel
icon = pygame.image.load(path("zusatz/icon.png"))
#https://www.clipartmax.com/png/middle/77-772018_thumbnail-for-version-as-of-classic-pac-man-artwork.png

#Eigene Datei?:---------------------------------
#Überprüfung, ob Sound möglich ist
try:
    sound, muted, VOLUME = True, False, 0.3
    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)

    #Soundeffekte
    soundeffekte_liste = [] #In die Klammeer mit " " ("Beispiel1", "Beispiel2"), also Auflistung der Soundeffekte
    soundeffekt = [pygame.mixer.Sound(path(f"zusatz/soundeffekte/{sound}.mp3")) for sound in soundeffekte_liste]
except: sound = False

def play_audio(audio=None):
    if sound:
       if not audio:
          musik = f"zusatz/Musik/{random.randint()}.mp3" #random.randint(1, wie viele Lieder).mp3 - Wählt zufällig eins aus
          pygame.mixer.music.load(path(musik))
          pygame.mixer.music.play(-1)
       else: soundeffekt[soundeffekte_liste.index(audio)].play()
#-------------------------------------------------

from pygame.math import Vector2 as vec

# screen settings
WIDTH, HEIGHT = 610, 670
FPS = 60
TOP_BOTTOM_BUFFER = 50
Karte_WIDTH, Karte_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

ROWS = 30
COLS = 28

# colour settings
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR = (190, 194, 15)

Schriftgroeße = 20
Schrift = 'arial'              #'Zusatz/Oswald-Bold.ttf'