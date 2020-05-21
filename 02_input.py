from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


def eventJoystick(joystick):
    print("eventJoystick() / " +
        "L: ({0:4}, {1:4}), {2:5}, {3:5} / ".format(joystick.left.x, joystick.left.y, joystick.left.direction.name, joystick.left.event.name) +
        "R: ({0:4}, {1:4}), {2:5}, {3:5}".format(joystick.right.x, joystick.right.y, joystick.right.direction.name, joystick.right.event.name))


if __name__ == '__main__':

    drone = Drone()
    drone.open("COM4")

    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Joystick, eventJoystick)

    drone.sendPing(DeviceType.Controller)

    for i in range(10, 0, -1):
        print(i)
        sleep(1)

    drone.close()
