from controller.py_sensor_controller import Controller
from model.py_sensor_model import Model, Status, Machine, MachineType
from view.py_sensor_view import View

# Create our controller
controller = Controller()

# Create an example machine
machine1 = Machine(1, MachineType.TREADMILL, [1, 1, 1])

# Add our example machine
controller.add_machine(machine1)

assert(controller.get_machines()[1] == machine1)

print("Success")

#create our view
view = View(controller.get_model())

view.print_machine_id(machine1)
view.print_machine_type(machine1)
view.print_machine_location(machine1)
view.print_machine_status(machine1)

assert(view.get_machines() == machine1)

print("Another Success")

