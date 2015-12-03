# Standard imports
import unittest

# Local imports
from controller.py_sensor_controller import Controller
from model.py_sensor_model import Model, Status, Machine, MachineType
from view.py_sensor_view import View


class TestBasicFunctions(unittest.TestCase):
	def setUp(self):
		# Create our controller
		self.controller = Controller()
	
		#create our view
		self.view = View(self.controller.get_model())
		
		# Create an example machine
		self.machine1 = Machine(1, MachineType.TREADMILL, [1, 1, 1])

	def testAddMachine(self):
		# Add our example machine
		self.controller.add_machine(self.machine1)

		self.assertEqual(self.controller.get_machines()[1], self.machine1)

	def testGetMachineType(self):
		# Add our example machine
		self.controller.add_machine(self.machine1)
		
		# self.view.print_machine_type(1)
		
	def testDisplayStatus(self):
		# Add our example machine
		self.controller.add_machine(self.machine1)
		
		final_string = self.view.format_line(["ID", "Machine Type"]) + \
			self.view.format_line([self.machine1.id, self.machine1.get_type()])
		
		self.assertEqual(self.view.display_status(), final_string)
		
"""
view.print_machine_id(1)
view.print_machine_type(1)
view.print_machine_location(1)
view.print_machine_status(1)

assert(view.get_machines() == 1)

print("Another Success")
"""

if __name__ == '__main__':
	unittest.main()