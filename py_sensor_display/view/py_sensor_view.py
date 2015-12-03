from model.py_sensor_model import Model
#from gi.repository import Gtk

class View():
	def __init__(self, model):
		self.model = model
		# win = Gtk.Window()
		# win.connect("delete-event", GTK.main_quit)
		# win.show_all()
		# GTK.main()

	def get_machines(self):
		return self.model.get_machines()
	
	def get_machine_status(self, id):
		return self.model.get_machine_status(id)
		
	def get_machine_location(self, id):
		return self.model.get_machine_location(id)
		
	def get_machine_type(self, id):
		return self.model.get_machine_type(id)
		
	def print_machines(self):
		print(self.get_machines())
	
	def print_machine_status(self, id):
		print(self.get_machine_status(id))
		
	def print_machine_location(self, id):
		print(self.get_machine_location(id))
		
	def print_machine_type(self, id):
		print(self.get_machine_type(id))
	
	def format_line(self, args):
		return "| {0:3} | {1:15} |\n".format(args[0], args[1])
		
	def display_status(self):
		final_string = self.format_line(["ID", "Machine Type"])
		
		for id in self.get_machines().keys():
			final_string += self.format_line([id, self.get_machine_type(id)])
			
		return final_string