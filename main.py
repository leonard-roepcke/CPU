print("CPU started")

#raise TypeError("TypeError")

from utils import *


cnt = Cnt()
ram = Ram()
cpu = Cpu(cnt, ram)


input = [
    [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1]],
    [[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,1]],
    [[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1]],
    [[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,1]],
    [[0,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1]],
]

adr = Safe_8bit()
data = Safe_8bit()
for i_adr, i_data in input:
    adr.write(i_adr)
    data.write(i_data)
    ram.write(adr.read(),data.read())

cpu.run()
