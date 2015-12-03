from model.py_sensor_model import Model
#from gi.repository import Gtk

class View():
	def __init__(self, model):
		self.model = Model()
		
	def get_machines(self):
		self.model.get_machines()
	
	def get_machine_status(self, id):
		self.model.get_machine_status(id)
		
	def get_machine_location(self, id):
		self.model.get_machine_location(id)
		
	def get_machine_type(self, id):
		self.model.get_machine_type(id)
		
	def print_machines(self):
		print(self.model.get_machines())
	
	def print_machine_status(self, id):
		print(self.model.get_machine_status(id))
		
	def print_machine_location(self, id):
		print(self.model.get_machine_location(id))
		
	def print_machine_type(self, id):
		print(self.model.get_machine_type(id))
		
	def print_machine_id(self, machine):
		print(machine.id)