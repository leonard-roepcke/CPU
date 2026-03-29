def add_1bit(bit_1, bit_2, carry=0):
    out_1 = bit_1 ^ bit_2 ^ carry
    carryer = (bit_1 and bit_2) or (bit_2 and carry) or (bit_1 and carry)
    return [out_1, carryer]
    
def add_8bit(a_8bit, b_8bit, carry=0):
    out_8bit = []
    for a_i, b_i in list(zip(a_8bit, b_8bit))[::-1]:
        out, carry = add_1bit(a_i, b_i, carry)
        out_8bit.append(out)
    return [out_8bit[::-1], carry]

class Safe_8bit:
    def __init__(self, n_8bit = [0,0,0,0,0,0,0,0]):
        self.n_8bit = n_8bit

    def write(self, n_8bit=[0,0,0,0,0,0,0,0]):
        self.n_8bit = n_8bit

    def read(self):
        return self.n_8bit

    def clear(self):
        self.write()

class Cnt:
    def __init__(self):
        self.n_8bit = Safe_8bit()

    def tick(self):
        np1 = add_8bit(self.n_8bit.read(),[0]*8,1)[0]
        self.n_8bit.write(np1)

    def read(self):
        return self.n_8bit.read()

    def reset(self):
        self.n_8bit.clear()

def control_unit(inp=[0]*8, data=[0]*8, safe_8bit=[0]*8):
    a_8bit = [0]*8
    b_8bit = [0]*8
    if inp==[0,0,0,0,0,0,0,0]:
        pass #write 0
    if inp==[0,0,0,0,0,0,0,1]:
        a_8bit = data 
    if inp==[0,0,0,0,0,0,1,0]:
        b_8bit = safe_8bit
    if inp==[0,0,0,0,0,0,1,1]:
        a_8bit = data
        b_8bit = safe_8bit
    if inp==[0,0,0,0,0,1,0,01:
        a_8bit = complement_8bit(data)
        b_8bit = safe_8bit
            
    return [a_8bit, b_8bit]

def complement_8bit(n_8bit):
    out = [n ^ 1 for n in n_8bit]
    return add_8bit(out, [0]*8, carry=1)
