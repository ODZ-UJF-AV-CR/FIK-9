#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import serial
import serial.tools.list_ports;
import sys

class Labdos:
	def __init__(self, file, baudrate):
		self._filename = file
		self._baudrate = baudrate
		for port in serial.tools.list_ports.comports():
			print(port, port.vid)
			if (port.vid == 1027):
				self._ser = serial.Serial(port.device, self._baudrate)
				time.sleep(0.1)
				self._ser.flush()
		if not hasattr(self, '_ser'):
			raise Exception

	def read(self, queue, read_timeout):
		t = time.time()
		while True:
			try:
				data = self._ser.readline().decode('utf-8', errors='replace').rstrip()
				self.write_data(data)
				self.write_counts(data, queue)
				t = time.time()
			except:
				if time.time() - t > read_timeout:
					queue.put(-1) # no data read for long period of time
					time.sleep(10)
					return -1

	def write_data(self, data):
		if (len(data) > 0):
			with open(self._filename, 'a') as f:
				f.write(str(time.time()) + ',' + data + '\n')

	def write_counts(self, data, queue):
		if (len(data) >= 240):
			data_lst = data.split(',')
			#data_lst = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,'kaccer', 21,321,654,564,654,321,654,321,687,4]
			try:
				counts = sum(list(map(int, data_lst[10:])))
				queue.put(counts)
			except:
				print(data_lst)
				queue.put(-2) # labdos counts could not be resolved from string

def start_LABDOS(queue, file, baud=115200):
	while True:
		serial_initialized = False
		while not serial_initialized:
			try:
				labdos = Labdos(file, baud)
				serial_initialized = True
				queue.put(999) # serial connection initialized
			except:
				queue.put(-3) # serial connection not initialized
				time.sleep(10)
		print('LABDOS serial connection was sucessfully initialized!')
		labdos.read(queue, 60)
