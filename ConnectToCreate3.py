import sys
import math
import threading
import time
from inputs import get_gamepad
# sys.path.append('/home/tyang/irobot-edu-python-sdk/irobot_edu_sdk/')
# sys.path.append('/home/tyang/irobot-edu-python-sdk/irobot_edu_sdk/backend/')
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
# from bluetooth import Bluetooth
# from robots import event, hand_over, Color, Robot, Root, Create3
create3_name = "iRobot-394CB78AD5364AAF93E145"
robot = Create3(Bluetooth(name=create3_name))

@event(robot.when_play)
async def play(robot):
    print('starting event trigger')
    # await play_one_up_tune()
    running = True
    robot_speed = 30
    while running:
        key = input("key: ")
        if (key == "q"):
            running = False
        if(key == "w"):
            vl = robot_speed
            vr = robot_speed
        if(key == "s"):
            vl = -robot_speed
            vr = -robot_speed
        if(key == "d"):
            vl = robot_speed
            vr = -robot_speed
        if(key == "a"):
            vl = -robot_speed
            vr = robot_speed
        await robot.set_wheel_speeds(vl, vr)
        time.sleep(0.5)
    sys.exit(0)
robot.play()