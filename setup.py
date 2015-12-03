from setuptools import setup

from py_sensor_display import __project__, __version__, CLI, DESCRIPTION

# TODO: Test this
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ''  # a placeholder, readme is generated on release


# TODO: Test this
if os.path.exists('CHANGES.rst'):
    CHANGES = open('CHANGES.rst').read()
else:
    CHANGES = ''  # a placeholder, changelog is generated on release

setuptools.setup(
    name=__project__,
    version=__version__,

    description=DESCRIPTION,
    url='https://github.com/tjdevries/py_sensor_display',
    author='tjdevries',
    author_email='devries.timothyj@gmail.com',

    packages=setuptools.find_packages(),

    # entry_points={
        # 'console_scripts': [CLI + ' = aecko.blend:main']
    # },

    long_description=(README + '\n' + CHANGES),
    # classifiers=[
        # 'Environment :: Console',
        # 'Intended Audience :: Other Audience',
        # 'License :: Freely Distributable',
        # 'Natural Language :: English',
        # 'Operating System :: OS Independent',
        # 'Programming Language :: Python :: 3.4',
        # 'Topic :: Multimedia :: Graphics',
    # ],

    # install_requires=[
        # 'natsort >= 4.0.3',
        # 'pillow >= 3.0.0',
        # 'numpy >= 1.10.1',
    # ],
)