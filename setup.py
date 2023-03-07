from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# make the scripts in the scripts folder executable
import sys
import os
for script in os.listdir('scripts'):
    os.chmod(os.path.join('scripts', script), 509)

d = generate_distutils_setup(
    packages=['package_name'],
    package_dir={'': 'src'}
)
setup(**d)