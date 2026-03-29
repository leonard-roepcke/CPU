print("CPU started")

raise TypeError("Hi")

from utils import *

inp = Safe_8bit([0,0,0,0,0,1,0,0])
a = Safe_8bit([1,0,0,0,0,0,0,1])
b = Safe_8bit([1,0,0,0,0,0,1,1])

a_c, b_c = control_unit(inp.read(), a.read(), b.read())
print(add_8bit(a_c, b_c))
