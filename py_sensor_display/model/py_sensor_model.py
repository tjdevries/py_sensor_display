"""
Model for our Python Sensor Display
Made for Engineering 325,
    but also for our senior design project.

    TJ DeVries
    Ryan Siekman
"""

# Standard Imports
from enum import Enum

class Model():
    def __init__(self):
        self.machines = {}

    def add_machine(self, machine):
        # Check if this ID has already been used.
        if self.get_machine_object(machine.id):
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
        if id in self.get_machines().keys():
            return self.machines[id]
        else:
            return None

    def get_machine_id(self, machine):
        return

class Status(Enum):
    UNKNOWN = 0
    OPEN = 1
    BUSY = 2
    RESERVED = 3
    OUT_OF_ORDER = 4

    def __str__(self):
        return self.name.capitalize()

    def color_string(self):
        """
        Returns the correct color start and finish sequence

        :returns: A list where the first entry is the start of a color sequence,
            and the second entry is the ending of the color sequence
        """
        color_start = '\033[00m'

        if self.name == "OPEN":
            color_start = '\033[32m'
        elif self.name == "BUSY":
            color_start = '\033[31m'

        return [color_start, '\033[00m']


class MachineType(Enum):
    TREADMILL = 1
    BICYCLE = 2

    def __str__(self):
        return self.name.capitalize()


class Machine():
    def __init__(self, id, type, location, color=False):
        self.id = id
        self.type = type
        self.location = location
        self.status = Status.UNKNOWN

        # Our variable that holds whether we will print in color or not
        self.color = color

    # Getters
    def get_id(self):
        return self.id

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

    # String representation
    def __str__(self):
        s = str(self.id)

        if self.color:
            status_color = self.get_status().color_string()
            s = status_color[0] + s + status_color[1]

        return s
