"""
Model for Py Sensor Display
"""

from enum import Enum

class Model():
	def __init__(self):
		self.machines = {}
		
	def add_machine(self, machine):
		if machine.id in self.machines.keys():
			raise Exception("Machine with this ID has already been added")

		self.machines[machine.id] = machine
		
	def remove_machine(self, id):
		del machines[id]
	
	# Getters
	
	def get_machines(self):
		return self.machines
	
	def get_machine_status(self, id):
		return self.machines[id].get_status()	
		
	def get_machine_location(self, id):
		return self.machines[id].get_location()
		
	def get_machine_type(self, id):
		return self.machines[id].get_type()
	
	# Setters
	
	def set_machine_status(self, id, status):
		self.machines[id].set_status(status)
		
	def set_machine_location(self, id, location):
		self.machines[id].set_location(location)		

	# maybe bad
	def get_machine_object(self, id):
		return self.machines[id]
		
	def get_machine_id(self, machine):
		return 
		
class Status(Enum):
	UNKNOWN = 0
	OPEN = 1
	BUSY = 2
	RESERVED = 3
	OUT_OF_ORDER = 4
	
class MachineType(Enum):
	TREADMILL = 1
	BICYCLE = 2
	
	def __str__(self):
		return self.name.capitalize()
		
	
class Machine():
	def __init__(self, id, type, location):
		self.id = id
		self.type = type
		self.location = location
		self.status = Status.UNKNOWN
	
	# Getters
	
	def get_status(self):
		return self.status
		
	def get_location(self):
		return self.location
		
	def get_type(self):
		return self.type
		
	# Setters
	def set_status(self, status):
		self.status = status
		
	def set_location(self, location):
		self.location = location