import time
import serial
import csv
import os

class Pited:
	def __init__(self, file, tty, baudrate):
		self._filename = file
		self._tty = tty
		self._baudrate = baudrate
		self._ser = serial.Serial(self._tty, baudrate=self._baudrate)
		time.sleep(0.1)
		self._ser.flush()

	def read(self, queue, read_timeout):
		t = time.time()
		while True:
			try:
				counts = self._ser.readline().decode('utf-8', errors='replace').rstrip()
				data = [str(time.time()), counts]
				self.save_data(data)
				queue.put(counts)
				t = time.time()
			#try:
				#k = 1
			except:
				if time.time() - t > read_timeout:
					queue.put(-1) # no data read for long period of time
					time.sleep(10)
					return -1

	def save_data(self, data):
		columns = ['time', 'pited_counts']
		#print(data)
		if not os.path.isfile(self._filename):
			with open(self._filename, 'w') as f:
				csvwriter = csv.writer(f)
				csvwriter.writerow(columns)
		with open(self._filename, 'a') as f:
			csvwriter = csv.writer(f)
			csvwriter.writerow(data)


def start_PiTED(queue, file, tty='/dev/ttySOFT0', baud=1200):
	while True:
		serial_initialized = False
		while not serial_initialized:
			try:
				pited = Pited(file, tty, baud)
				serial_initialized = True
				queue.put(999) # serial connection initialized
			except:
				queue.put(-3) # serial connection not initialized
				time.sleep(10)
		print('PiTED serial connection was sucesfully initiated!')
		pited.read(queue, 60)
