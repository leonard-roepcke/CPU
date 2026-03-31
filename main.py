print("CPU started")

#raise TypeError("TypeError")

from utils import *

ram = Ram_8byte()
ram.write([0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1])
a = Safe_8bit([0,0,0,0,0,0,0,0])

for i in range(8):
    print(a.read() , "   " , ram.read(a.read()))
    a.write(add_8bit(a.read(),[0,0,0,0,0,0,0,1])[0])

"""
a = Safe_8bit()
inp = Safe_8bit()
b = Safe_8bit()

while True:
    inp.write(player_inp_8bit("Control bits: "))
    a.write(player_inp_8bit("data bits: "))

    a_c, b_c = control_unit(inp.read(), a.read(), b.read())
    b.write(add_8bit(a_c, b_c)[0])

    print(b.read())
"""
