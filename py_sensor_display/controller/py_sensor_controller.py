from model.py_sensor_model import Model

class Controller():
	def __init__(self):
		# Create our model
		self.model = Model()
		
	def add_machine(self, machine):
		self.model.add_machine(machine)
		
	def remove_machine(self, id):
		self.model.remove_machine(id)
	
	# Getters
	def get_machines(self):
		return self.model.get_machines()
		
	def get_machine_object(self, id):
		return self.model.get_machine_object(id)
	
	def get_machine_status(self, id):
		return self.model.get_machine_status(id)
	
	# Setters
	def set_machine_status(self, id, status):
		self.model.set_machine_status(id, status)
		
	def set_machine_location(self, id, location):
		self.model.set_machine_location(id, location)
		
	def get_model(self):
		return self.model