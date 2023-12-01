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

the_connection = mavutil.mavlink_connection('/dev/ttyUSB0',baud=57600,source_system=200,source_component=138)

#the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
#                                              mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)


while True:
  msg = the_connection.recv_match(blocking=True)
  print("MSG:",msg.get_type())
  if msg.get_type() == "BAD_DATA":
     print(msg.data)

  
