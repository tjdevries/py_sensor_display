from controller.py_sensor_controller import Controller
from model.py_sensor_model import Model, Status, Machine, MachineType

# Create our controller
controller = Controller()

# Create an example machine
machine1 = Machine(0, MachineType.TREADMILL, [1, 1, 1])

# Add our example machine
controller.add_machine(machine1)

assert(controller.get_machine_object(0) == machine1)

print("Success")
