#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example test.

Made by: TJ DeVries and Ryan Siekman

This ideally will be the example we use for the presentation in 325
"""

# Local Imports
from controller.py_sensor_controller import Controller
from model.py_sensor_model import Model, Status, MachineType, Machine
from view.py_sensor_view import View
from basic_test import TestBasicFunctions
def main():
    """
    The main loop for the test
    :returns: None
    """
    # Begin our function by declaring a controller and a view
    controller = Controller()

    # Create our view
    view = View(controller.get_model())

    welcome(controller, view)
    return None

def welcome(controller, view):
    """
    The welcome and setup function for the test

    :controller: The controller created in the main loop
    :view: The view created in the main loop

    :returns: TODO

    """
    # Add our first machine
    machine1 = Machine(1, MachineType.BICYCLE, [1, 1, 1], True)
    machine1.set_status(Status.OPEN)
    controller.add_machine(machine1)

    # Add our second machine
    machine2 = Machine(2, MachineType.TREADMILL, [2, 3, 5], True)
    controller.add_machine(machine2)
    machine2.set_status(Status.BUSY)

    # Add our third machine
    machine3 = Machine(17, MachineType.BICYCLE, [3, 13, 10], True)
    controller.add_machine(machine3)

    # Add our fourth machine
    machine4 = Machine(12, MachineType.BICYCLE, [1, 2, 3], True)
    controller.add_machine(machine4)

    # Add our fifth machine
    machine5 = Machine(7, MachineType.BICYCLE, [5, 6, 1], True)
    controller.add_machine(machine5)

    print(view.display_locations())


if __name__ == "__main__":
    main()
