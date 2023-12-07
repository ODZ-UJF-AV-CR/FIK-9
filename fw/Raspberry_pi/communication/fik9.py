import time
import serial
from multiprocessing import Process, Queue
from pited import start_PiTED
from labdos import start_LABDOS
import subprocess
from pymavlink import mavutil

def empty_queue(q, q_px, label):
	while True:
		msg = q.get()
		msg_dict[label] = msg
		q_px.put((label, msg))
		print(label, msg)

def read_tpx(queue, file):
	while True:
		str = "tail -n 1 " + file
		try:
			counts = subprocess.check_output(str, shell=True)
			counts = counts.decode('ASCII')
			data_file, tm, counts = counts.split(' ')
			counts = int(counts)
			queue.put(counts)
		except:
			queue.put(-1)
		finally:
			time.sleep(10)

def mavlink_init():
	conn = mavutil.mavlink_connection('/dev/ttyS0', baud=9600, source_system=1, source_component=138)
	conn.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
				mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
	conn.wait_heartbeat()
	print('Heartbeat ok')
	return conn

def px4_send_simulator(q_px):
	temp_dict = {'labdos':[0, 4],
			 'timepix':[4, 8],
			 'pited':[8, 12],
			 'spacepix':[12, 16]}
	msg = bytearray(128)
	while True:
		(label, count) = q_px.get()
		print('px4_sim', label, count)
		rng = temp_dict[label]
		try:
			msg[rng[0]:rng[1]] = int(count).to_bytes(4, 'big', signed=True)
		except:
			k = 1
		print(msg)
		time.sleep(5)

def px4_send(q_px):
	while True:
		temp_dict = {'labdos':[0,4],
			 'timepix':[4,8],
			'pited':[8,12], 
			'spacepix':[12,16]}
		try:
			conn = mavlink_init()
		except:
			continue

		msg = bytearray(128)
		while True:
			try:
				conn.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
					mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
				(label, count) = q_px.get()
				rng = temp_dict[label]
				msg[rng[0]:rng[1]] = int(count).to_bytes(4, 'big', signed=True)
				print(msg)
				conn.mav.tunnel_send(target_system=0, target_component=0,
					 payload_type=305, payload_length=1, payload=msg)
			except:
				k = 1
			finally:
				time.sleep(5)
msg_dict = {'labdos': 3, 'timepix': 145, 'pited': 230.652, 'spacepix': 1295}

labdos_file = 'labdos.csv'
pited_file = 'pited.csv'
tpx_file = 'tpx.csv'
	
px4_queue = Queue()
px4_p = Process(target=px4_send, args=(px4_queue,))
#px4_p = Process(target=px4_send_simulator, args=(px4_queue,))
px4_p.start()

pited_queue = Queue()
pited_p = Process(target=start_PiTED, args=(pited_queue,pited_file))
pited_empty = Process(target=empty_queue, args=(pited_queue, px4_queue,'pited'))
pited_p.start()
pited_empty.start()

labdos_queue = Queue()
labdos_p = Process(target=start_LABDOS, args=(labdos_queue, labdos_file, 115200))
labdos_empty = Process(target=empty_queue, args=(labdos_queue, px4_queue, 'labdos'))
labdos_p.start()
labdos_empty.start()

tpx_queue = Queue()
tpx_p = Process(target=read_tpx, args=(tpx_queue, tpx_file))
tpx_empty = Process(target=empty_queue, args=(tpx_queue, px4_queue, 'timepix'))
tpx_p.start()
tpx_empty.start()

px4_p = Process(target=px4_send_simulator, args=(px4_queue,))

