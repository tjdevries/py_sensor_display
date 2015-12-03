from model.py_sensor_model import Model

class Controller():
	def __init__(self):
		# Create our model
		self.model = Model()
		
	def add_machine(self, machine):
		self.model.add_machine(machine)
		
	def remove_machine(self, machine):
		pass
		
	def get_machine_object(self, id):
		pass
	
	def get_machine_status(self, machine):
		pass
		
	def set_machine_status(self, machine, status):
		pass
		
	def set_machine_location(self, machine, location):
		pass