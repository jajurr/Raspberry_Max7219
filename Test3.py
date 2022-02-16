import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from MyMax7219 import MyMatrix
from random import randint
import time

matrix = MyMatrix()

intRichtung = 0
modulu = 0

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def steuerung(gpio):
    global intRichtung, modulu, richtung
    print(gpio)
    if (gpio == 11):
        print("Button 11 was pushed!")
        intRichtung = intRichtung + 1
    if (gpio == 12):
        print("Button 12 was pushed!")
        intRichtung = intRichtung + 3
    modulu = intRichtung % 4
    print("intRichtung")
    print(intRichtung)
    print("modulu:")
    print(modulu)
    if modulu == 0:
        richtung = [0, -1]
    if modulu == 1:
        richtung = [-1, 0]
    if modulu == 2:
        richtung = [0, 1]
    if modulu == 3:
        richtung = [1, 0]

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(11, GPIO.FALLING, callback=steuerung)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(12, GPIO.FALLING, callback=steuerung)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
	
def startSpiel():
  global snake, richtung, apfel
  snake = [[randint(2,width-4),randint(3,height-3)]]
  richtung = [0,0]
  while richtung == [0,0]:
    matrix.show_message("READY")
  neuerApfel()

def neuerApfel():
  global apfel, snake
  apfelSnake = False
  while apfelSnake == False:
    apfelSnake = True
    apfel = [randint(0,width),randint(0,height)]
    for i in snake:
      if(i == apfel):
        apfelSnake = False
  print(apfel)


def endOfGame():
  for i in range(0,2):
    matrix.clear()
    for i in range(0,width+1):
      for j in range(0,height+1):
        matrix.pixel(i,j,1)
        time.sleep(0.001)
    time.sleep(0.01)
  matrix.show_message("GAME OVER")
  punkte = len(snake)-1
  matrix.show_message(str(punkte)+" PUNKTE")

  startSpiel()

startSpiel()

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


  if(snake[0][0] > width or snake[0][1] > height
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