from utils import *
print("Compilor started")
program_bin = []
write_adr_cnt = Cnt()
write_adr_cnt.tick(2)

comand_map = {
    "stp":"00000000" #program stop
    "wrt":"00000001" #override
    "sty":"00000010" #stays the same (pass)
    "add":"00000011" #adds to data
    "sub":"00000100" #subtracts to data
    "jmp":"00000101" #jumps to adr
}
with open("program.txt") as f:
    program = f.read()

program_started = False
for line in program:
    if line == "start": program_stared = True
    if not program_stared: continue
    
program_bin.append("00000001 00000000")
program_bin.append("00000000 00000001")
with open("program_bin.txt", "w") as bin_f:
    bin_f.write("".join(program_bin))
