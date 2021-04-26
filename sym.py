from sympy import *
from sympy.physics.units.quantities import Quantity
r = Symbol("r")
a = Quantity("a")
print(integrate((r**2 + r*a + a**2)*DiracDelta(r- a)**3, (r, -1, 1.0)))    
