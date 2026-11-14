
import math

def read_imu(bno):
    deadSensor = False
    try:
        x, y, z, w = bno.quaternion
    except (RuntimeError, OSError):
        x, y, z, w = 0.0, 0.0, 0.0, 0.0
        deadSensor = True

    if x == 0.0 and y == 0.0 and z == 0.0 and w == 0.0:
        deadSensor = True

    imuInfo = {}
    roll = math.degrees(math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y)))
    if (2 * (w * y - z * x)) > 1:
        pitch = 90.0
    elif (2 * (w * y - z * x)) < -1:
        pitch = -90.0
    else:
        pitch = math.degrees(math.asin(2 * (w * y - z * x)))
    yaw = math.degrees(math.atan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z)))
    heading = yaw % 360
    if deadSensor:
        imuInfo['heading'] = -1.0
        imuInfo['roll'] = 0.0
        imuInfo['pitch'] = 0.0
    else:
        imuInfo['roll'] = roll
        imuInfo['pitch'] = pitch
        imuInfo['heading'] = heading
    return imuInfo
    