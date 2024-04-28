# imports `main_2` module from root, irrespective whether `pkg1\main_2.py` exists
import main_2

# imports `main_2` module from current pkg
from . import main_2