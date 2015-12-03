from model.py_sensor_model import Model
#from gi.repository import Gtk

class View():
	def __init__(self, model):
		self.model = Model()
		
	def get_machines(self):
		self.model.get_machines()
	
	def get_machine_object(self, id):
		self.model.get_machine_object(id)
	
	def get_machine_status(self, machine):
		self.model.get_machine_status(machine)
		
	def get_machine_location(self, machine):
		self.model.get_machine_location(machine)
		
	def get_machine_type(self, machine):
		self.model.get_machine_type(machine)
		
	def get_machine_id(self, machine):
		self.model.get_machine_id(machine)
		
	def print_machines(self):
		print(self.model.get_machines())
	
	def print_machine_object(self, id):
		print(self.model.get_machine_object(id))
	
	def print_machine_status(self, machine):
		print(self.model.get_machine_status(machine))
		
	def print_machine_location(self, machine):
		print(self.model.get_machine_location(machine))
		
	def print_machine_type(self, machine):
		print(self.model.get_machine_type(machine))
		
	def print_machine_id(self, machine):
		print(self.model.get_machine_id(machine))