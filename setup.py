from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['eye_display'],
    package_dir={'': 'rosserial_ex'},
)

setup(**d)
