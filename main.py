print("CPU started")

from utils import *

cnt = Cnt()
ram = Ram()
cpu = Cpu(cnt, ram)

programm_bin = import_bin()

#input loop values temp
adr = Safe_8bit()
data = Safe_8bit()

for i_adr, i_data in programm_bin:
    adr.write(i_adr)
    data.write(i_data)
    ram.write(adr.read(),data.read())

cpu.run()
