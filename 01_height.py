from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

height = 0;
    

def eventAltitude(altitude):
    print("eventAltitude()")
    print("-  Temperature: {0:.3f}".format(altitude.temperature))
    print("-     Pressure: {0:.3f}".format(altitude.pressure))
    print("-     Altitude: {0:.3f}".format(altitude.altitude))
    print("- Range Height: {0:.3f}".format(altitude.rangeHeight))
    global height
    height = altitude.rangeHeight;
    
    
if __name__ == '__main__':

    drone = Drone()
    drone.open("COM4")
    
    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Altitude, eventAltitude)

    # Altitude 정보 요청
    while 1:
        drone.sendRequest(DeviceType.Drone, DataType.Altitude)
        print(height)
        sleep(0.1)
        if height > 0.4:
            
            break;
    drone.close();
    
