import RPi.GPIO as GPIO # Importiert die Raspberry Pi GPIO library
from MyMax7219 import MyMatrix # Greift auf MxMax7219 zu
from random import randint # Importiert random Library
import time # Importiert time Library


matrix = MyMatrix() #Erzeugt Matrix Objekt

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

#Regelt die Steuerung der Schlange
def steuerung(gpio):
    global richtung

    if richtung == [0,0]: #Noch keine Richtung
        if gpio == 11:
            richtung = [-1,0]
            return
        if gpio == 12:
            richtung = [1,0]
            return

    if richtung == [0, -1]: #oben
        if gpio == 11:
            richtung = [-1,0]
            return
        if gpio == 12:
            richtung = [1,0]
            return

    if richtung == [-1, 0]: #links
        if gpio == 11:
            richtung = [0, 1]
            return
        if gpio == 12:
            richtung = [0, -1]
            return

    if richtung == [0, 1]: #unten
        if gpio == 11:
            richtung = [1, 0]
            return
        if gpio == 12:
            richtung = [-1, 0]
            return

    if richtung == [1, 0]: #rechts
        if gpio == 11:
            richtung = [0, -1]
            return
        if gpio == 12:
            richtung = [0, 1]
            return

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Setzt den Pin 11 auf Input mit Pull-Down
GPIO.add_event_detect(11, GPIO.FALLING, callback=steuerung) #Ruft die 'steuerung' Methode aus, bei Knopfdruck

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Setzt den Pin 12 auf Input mit Pull-Down
GPIO.add_event_detect(12, GPIO.FALLING, callback=steuerung) #Ruft die 'steuerung' Methode aus, bei Knopfdruck

#Startet das Spiel
def startSpiel():
  global snake, richtung, apfel
  snake = [[randint(2,4),randint(3,5)]]
  richtung = [0,0]
  while richtung == [0,0]:
      matrix.pixel(1, 1, 1)
      time.sleep(0.1)
      matrix.pixel(1, 1, 0)
  neuerApfel()

#Erstellt einen neuen Apfel
def neuerApfel():
  global apfel, snake
  apfelSnake = False
  while apfelSnake == False:
    apfelSnake = True
    apfel = [randint(0,7),randint(0,7)]
    for i in snake:
      if(i == apfel):
        apfelSnake = False
  print(apfel)

#SpielEnde
def endOfGame():
  for i in range(0,2):
    matrix.clear()
    for i in range(0,8):
      for j in range(0,8):
        matrix.pixel(i,j,1)
        time.sleep(0.001)
    time.sleep(0.01)
  print("GAME OVER")
  punkte = len(snake)-1
  print(str(punkte)+" PUNKTE")

  startSpiel()

startSpiel()

#Dauerschleife
while True:
  keinePause = False
  newSnake = [snake[0][0]+richtung[0],
              snake[0][1]+richtung[1]]
  for i in snake:
    if(i == newSnake):
      endOfGame()
      pass

  if(newSnake == apfel):
     neuerApfel()
     keinePause = True
  else:
     snake.pop()
  snake.insert(0,newSnake)

#Prüft nach Spielende
  if(snake[0][0] > 7 or snake[0][1] > 7
	or snake[0][0] < 0 or snake[0][1] < 0 ):
    endOfGame()
    pass

  matrix.clear()
  for i in snake:
    matrix.pixel(i[0],i[1], 1)
  matrix.pixel(apfel[0],apfel[1],1)
  if(keinePause == False):
    newLength = (len(snake)-2)*0.01
    time.sleep(0.3-newLength)
  else:
    time.sleep(0.3)