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

the_connection = mavutil.mavlink_connection('/dev/ttyS0',baud=9600,source_system=1,source_component=138)

the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                              mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

while True:
  # Send heartbeat from a MAVLink application. 
  the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

  #
  payload=bytearray(128)
  the_connection.mav.tunnel_send(target_system=0,target_component=0,payload_type=305,payload_length=1,payload=payload)
  #the_connection.mav.debug_send(time_boot_ms=15,ind=5,value=0.15)
  
  the_connection.wait_heartbeat()
  print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))
