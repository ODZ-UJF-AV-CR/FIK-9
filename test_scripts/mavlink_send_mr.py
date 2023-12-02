##nainstalovat s rozbitím systému
#sudo apt install python3-pip
#sudo apt install libxml2-dev libxslt-dev python3-serial
#pip3 install pymavlink --break-system-packages
#
##povolit seriovku
#sudo raspi-config
# 
##spustit
##MAVLINK20=1 python3 mavlink.py 

from pymavlink.dialects.v20 import common as mavlink2
from pymavlink import mavutil
import time

the_connection = mavutil.mavlink_connection('udpout:127.0.0.1:14445',source_system=200,source_component=138)

the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                              mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)




while True:
    the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    time.sleep(2)
    payload=bytearray(128)
    for i in range(128):
      payload[i]=i
    the_connection.mav.tunnel_send(target_system=0,target_component=0,payload_type=305,payload_length=1,payload=payload)
    time.sleep(2)
