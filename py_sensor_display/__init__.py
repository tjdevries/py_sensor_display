"""Package for py_sensor_display"""
# System
import sys
import os.path

__project__ = 'Python Sensor Display'
__version__ = '0.1'

CLI = 'py_sensor_display'
VERSION = '{0} v{1}'.format(__project__, __version__)
DESCRIPTION = 'Display the information about the sensor network'

MIN_PYTHON_VERSION = 3, 3

if not sys.version_info >= MIN_PYTHON_VERSION:
    exit("Python {}.{}+ is required.".format(*MIN_PYTHON_VERSION))

# Local
try:
    pass
except ImportError:
    pass