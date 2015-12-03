"""
Model for Py Sensor Display
"""

from enum import Enum

class Model():
	def __init__(self):
		self.machines = {}
		
	def add_machine(self, machine):
		machines[machine.id] = machine
		
	def remove_machine(self, id):
		del machines[id]
	
	def get_machines(self):
		pass
	
	def get_machine_object(self, id):
		pass
	
	def get_machine_status(self, machine):
		pass	
		
	def set_machine_status(self, machine, status):
		pass
		
	def set_machine_location(self, machine, location):
		pass	
		
	def get_machine_location(self, machine):
		pass
		
	def get_machine_type(self, machine):
		pass
		
	def get_machine_id(self, machine):
		pass	
		
class Status(Enum):
	UNKNOWN = 0
	OPEN = 1
	BUSY = 2
	RESERVED = 3
	OUT_OF_ORDER = 4
	
class MachineType(Enum):
	TREADMILL = 1
	BICYCLE = 2
	
class Machine():
	def __init__(self, id, type, location):
		self.id = None
		self.type = None
		self.location = None
		self.status = Status.UNKNOWN