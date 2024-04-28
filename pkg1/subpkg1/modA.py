# import from current subpkg of the same package
from .modB import func
from . import modB
from ..subpkg1 import modB

# importing from another subpkg of the same package
from ..subpkg2 import modD
from ..subpkg2.modD import func

# importing from immediate parent package of currrent subpkg
from .. import modC
from ..modC import func

# importing module from root even if current subpkg has module of the same name
import modB