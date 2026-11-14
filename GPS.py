import adafruit_gps
import time
 
def start_gps(uart):
    gps = adafruit_gps.GPS(uart)
    time.sleep(1)
    gps.send_command(b"PMTK314,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    time.sleep(1)
    gps.send_command(b"PMTK220,100")
    time.sleep(1)
    return gps

def read_gps(gps):
    exitCondition = True
    while exitCondition:
        try:
            exitCondition = gps.update() is not False
        except ValueError:
            continue

    gpsInfo = {}

    if gps.fix_quality == 0:
            gpsInfo['lat'] = 0.0
            gpsInfo['lon'] = 0.0
            gpsInfo['hdop'] = 99.99
            gpsInfo['sats'] = 0
            gpsInfo['fix'] = 0
    else:
        try:
            gpsInfo['lat'] = float(gps.latitude)
            gpsInfo['lon'] = float(gps.longitude)
            gpsInfo['fix'] = int(gps.fix_quality)
            gpsInfo['sats'] = int(gps.satellites)
            gpsInfo['hdop'] = float(gps.horizontal_dilution)
        except TypeError:
            gpsInfo['lat'] = 0.0
            gpsInfo['lon'] = 0.0
            gpsInfo['fix'] = 0
            gpsInfo['sats'] = 0
            gpsInfo['hdop'] = 99.99

    return gpsInfo
