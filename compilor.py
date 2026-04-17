from utils import *
print("Compilor started")
program_bin = []
write_adr_cnt = Cnt()
write_adr_cnt.tick(2)

comand_map = {
    "stp":"00000000", #program stop
    "wrt":"00000001", #override
    "sty":"00000010", #stays the same (pass)
    "add":"00000011", #adds to data
    "sub":"00000100", #subtracts to data
    "jmp":"00000101", #jumps to adr in register                          #fix adressing
    "skp":"00000110", #conditional skip if data > register x    
    "put":"00000111", #push to register x
    "pul":"00001000", #pull form register x to data
    "atr":"00001001", #next adresse to register
    "prr":"00001010", #print register
}
with open("program.txt", encoding="utf-8") as f:
    program = f.readlines()

program_started = False
for line in program:
    line_parts = line.strip().split()
    if line.strip() == "start":
        program_started = True
        continue
    if not program_started:
        continue
    program_bin.append(f"{bin_to_str(write_adr_cnt.read())} {comand_map[line_parts[0]]}")
    write_adr_cnt.tick()
    program_bin.append(f"{bin_to_str(write_adr_cnt.read())} {hex_to_bin(line_parts[1])}")
    write_adr_cnt.tick()
    
program_bin.append("00000001 00000000")
program_bin.append("00000000 00000001")
with open("program_bin.txt", "w") as bin_f:
    bin_f.write("\n".join(program_bin))
