# Py Sensor Display

Professor Michmerhuizen,

Below is the report regarding the project proposal described in this [document](https://github.com/tjdevries/py_sensor_display/blob/master/docs/proposal.md). This report was created in response to the final project for the Engineering 325 Lab. This report was created by TJ DeVries and Ryan Siekman.

## Goals of the project

Ryan and TJ set out to create a basic example of a [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (MVC) that would be used in their Senior Design project. This design must create the framework for a gym reservation system. The View portion must incorporate elements of GTK, which neither Ryan nor TJ have had experience on previously. The system must be light enough to run off of a Raspberry Pi.

This MVC must be capable of taking in machine specifications, such as type (treadmill versus bicycle), status (open versus reserved), location in the gym and an identification number (ID). Once an input has been given to the system, through the use of a GTK graphical user interface (GUI), the user should be able to see the status of all the machines. This status should be displayed in such a way that the average user can easily determine where a machine is located in the gym.

This project must be testable, as there will be several other modules that must be built around  and on top of the development done for this project. Testing must be demonstrated on several, if not all, applicable functions in some automated way.

## Resources Used

The resources can be categorized primarily in two ways. The first are software tools. The team used Git to collaborate and work on separate features of the project simultaneously. Additionally, the team used Python 3.4 and its built-in libraries to design and create the project.

The second category are hardware tools. This is the Raspberry Pi that the team showed the project could be run on. However, the implementation is quite platform agnostic and will work on a wide range of machines, provided that machine has a working Python 3.4 interpreter and can use Gtk to produce windows.

## What the Team Learned

There were two main areas that the team showed marked improvement in. 

### Test Driven Development

The first area was in regards to test driven development. Many of the classes and functions were defined with a `pass` statement, and then tests were written for expected output. Once the tests were written, code was developed in order to fulfill the testing requirements. Both TJ and Ryan had little experience doing this in a group setting. It was very helpful for ensuring that not only was code reliable, but also ensuring that all aspects of the code were modular and written in the smallest logical subsections.

An example of the strategy the team implemented is described below.

Two classes were defined before work on the testing began. These classes were `Model` and `Controller` (the **M** and the **C** of MVC, respectively). They each were given a function called `add_machine`, which was originally designed with a `pass`. This is shown in the following code block.

```python
class Model:
    def __init__(self, ...):
        # Code here

    def add_machine(self, machine):
        pass

class Controller:
    def __init__(self, model):
        # Code here
        self.model = model

    def add_machine(self, machine):
        pass
```

At this point, the two functions of `add_machine` do not do anything. Even so, tests were written for them in our testing file. A few of the tests are described below.

```python
class TestBasicFunctions(unittest.TestCase):
    def SetUp(self): 
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

    def testAddMachine_DuplicateMachine(self):
        # Add our first machine
        self.controller.add_machine(self.machine1)

        # Try to add the same machine, should fail
        self.assertRaises(Exception, self.controller.add_machine, self.machine1)
```

If you are not familiar with the unittest library in Python, do not worry about that .The main idea is that the team was trying to test that first, the system was  capable of adding a machine to the model, and second, that it would not take duplicate machines into the model (machines can't exist in two places!). 

Obviously at this point, these tests will fail. Neither of the `add_machine` methods do anything at all. So the team began developing the functionality required by the tests. Eventually, the team arrived at the following code. These implementations can be seen in their final form, with the other initialization and methods here: [model](https://github.com/tjdevries/py_sensor_display/blob/master/py_sensor_display/model/py_sensor_model.py), [controller](https://github.com/tjdevries/py_sensor_display/blob/master/py_sensor_display/controller/py_sensor_controller.py).

```python
class Model():
    def __init__(self):
        self.machines = {}

    def add_machine(self, machine):
        # Check if this ID has already been used.
        if self.get_machine_object(machine.id):
            raise Exception("Machine with this ID has already been added")

        self.machines[machine.id] = machine


class Controller():
    def __init__(self):
        # Create our model
        self.model = Model()

    def add_machine(self, machine):
        # Add the machine to our model
        self.model.add_machine(machine)
```

Once these (and the other tests and implementations were created) we could run our [basic_test.py](https://github.com/tjdevries/py_sensor_display/blob/master/py_sensor_display/basic_test.py) and receive the following results (at the time of completion of this report):

```
$ python3 basic_test.py

......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

This was really exciting for the team because now the team was able to be quite sure that the project met all of the goals that were set for it.

### MVC + GTK

Neither of the two team members had ever worked with a combination of MVC and GTK. In fact, neither of the team members really had an experience with GTK at all. This allowed for a lot of learning and preparation for the senior design project, where there will be a significant amount of work required in the area of UI development to ensure that our project is easy to use.

GTK modules are what makes the majority of GUI's used in Linux systems. It is modular and very useful for almost any application. It worked well in this case since each machine could be shown as it's own individual button, enabling an easy way to interact with the GUI created. In combination with MVC, it provides a way to create several different types of views -- for example the text view and the GUI view shown in this project's code -- while still using the same model and controller. This allows for a much more stable system, since each element uses the same backend for all of the processing.

## Conclusion

Ultimately, the team felt that they met all the goals that were originally proposed for the project. Both of the team members learned a lot of new information, both in the form of processes for development as well as actual implementation strategies. This was not only good practice for the lab, but also really helped the team get a good start on the development side of their Senior Design project.

All the code is freely available for viewing at the project's [github](https://github.com/tjdevries/py_sensor_display/).
