from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

leftX = 0;
leftY = 0;
rightX = 0;
rightY = 0;
leftName = 0;
rightName = 0;
buttonState = " "
buttonName = 0
#motorSpeed = 0  모터 회전속도 파악용 (takeOff / Landing) 구별용

#def eventMotion(motion):
#    global motorSpeed
#    motorSpeed = motion.accelX

def eventJoystick(joystick):
    # print("eventJoystick() / " +
    #    "L: ({0:4}, {1:4}), {2:5}, {3:5} / ".format(joystick.left.x, joystick.left.y, joystick.left.direction.name, joystick.left.event.name) +
    #    "R: ({0:4}, {1:4}), {2:5}, {3:5}".format(joystick.right.x, joystick.right.y, joystick.right.direction.name, joystick.right.event.name))
    global leftX
    global leftY
    global leftName
    global rightX
    global rightY
    global rightName
    leftX = joystick.left.x
    leftY = joystick.left.y
    leftName = joystick.left.direction.name
    rightX = joystick.right.x
    rightY = joystick.right.y
    rightName = joystick.right.direction.name
    
def eventButton(button):
    #print("eventButton() / " +
    #    "Button: 0b{0:16}, Event: {1:6}".format(bin(button.button)[2:].zfill(16), button.event.name))
    global buttonState
    global buttonName
    buttonState = button.event.name
    buttonName = button.button

def opByJoystick():
        drone.sendControlWhile(rightX, rightY, leftX, leftY,100)
        if buttonState == "Press":
            sleep(1)
            if buttonState == "Press":
                if buttonName == 2:
                    drone.sendLanding()
                elif buttonName == 1:
                    drone.sendTakeOff()
    
    
if __name__ == '__main__':

    drone = Drone()
    drone.open()

    # 조이스틱 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Joystick, eventJoystick)
    drone.sendPing(DeviceType.Controller)
    #버튼 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Button, eventButton)
    drone.sendPing(DeviceType.Controller)
    #가속도 핸들링
    #drone.setEventHandler(DataType.Motion, eventMotion)
    #drone.sendRequest(DeviceType.Drone, DataType.Motion)
    
    while True:
        if buttonState == "Press":
            sleep(1)
            if buttonState == "Press":
                if buttonName == 1:
                    drone.sendTakeOff()
                    break;

    while True:
        opByJoystick()
        
    drone.close()



