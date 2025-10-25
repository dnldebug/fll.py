from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
me = Motor(Port.F, Direction.COUNTERCLOCKWISE)
md = Motor(Port.B)
mt_crema = Motor(Port.E)
mt_cremaII = Motor(Port.A)

drive_base = DriveBase(me, md, 57, 57) 
drive_base.use_gyro(True) 

def andar(dist):
    drive_base.settings(350, 350, 220, 220)
    drive_base.straight(-dist*10)

def turn(radius, angle):
    drive_base.settings(200, 200, 200, 200)
    drive_base.curve(radius, angle)

def rotate(graus):
    drive_base.settings(220, 220, 220, 220)
    drive_base.turn(graus)
