def add_1bit(bit_1, bit_2, carry=0):
    catch_error(bit_1, int,  message="bit_1")
    catch_error(bit_2, int, message="bit_2")
    catch_error(carry, int, message="carry")

    out_1 = bit_1 ^ bit_2 ^ carry
    carryer = (bit_1 and bit_2) or (bit_2 and carry) or (bit_1 and carry)
    return [out_1, carryer]
    
def add_8bit(a_8bit, b_8bit, carry=0):
    catch_error(a_8bit, message="n_8bit")
    catch_error(b_8bit, message="n_8bit")
    catch_error(carry,int, message="n_8bit")


    out_8bit = []
    for a_i, b_i in list(zip(a_8bit, b_8bit))[::-1]:
        out, carry = add_1bit(a_i, b_i, carry)
        out_8bit.append(out)
    return [out_8bit[::-1], carry]

class Safe_8bit:
    def __init__(self, n_8bit = [0,0,0,0,0,0,0,0]):
        catch_error(n_8bit, message="n_8bit")

        self.n_8bit = n_8bit

    def write(self, n_8bit=[0,0,0,0,0,0,0,0]):
        catch_error(n_8bit, message="n_8bit")

        self.n_8bit = n_8bit

    def read(self):
        return self.n_8bit

    def clear(self):
        self.write()

class Cnt:
    def __init__(self):
        self.n_8bit = Safe_8bit()

    def tick(self):
        np1 = add_8bit(self.n_8bit.read(),[0,0,0,0,0,0,0,0],1)[0]
        self.n_8bit.write(np1)

    def read(self):
        return self.n_8bit.read()

    def reset(self):
        self.n_8bit.clear()

def control_unit(inp=[0,0,0,0,0,0,0,0], data=[0,0,0,0,0,0,0,0], safe_8bit=[0,0,0,0,0,0,0,0]):
    catch_error(inp, message="inp")
    catch_error(data, message="date")
    catch_error(safe_8bit, message="safe_8bit")



    a_8bit = [0,0,0,0,0,0,0,0]
    b_8bit = [0,0,0,0,0,0,0,0]
    if inp==[0,0,0,0,0,0,0,0]:
        b_8bit = safe_8bit
        #hier ist ein programm abbruch, das steht jedoch in der cpu
    if inp==[0,0,0,0,0,0,0,1]:
        a_8bit = data
        #write input 
    if inp==[0,0,0,0,0,0,1,0]:
        pass #clear set 0
    if inp==[0,0,0,0,0,0,1,1]:
        a_8bit = data
        b_8bit = safe_8bit
        #add input
    if inp==[0,0,0,0,0,1,0,0]:
        a_8bit = complement_8bit(data)
        b_8bit = safe_8bit
        #minus input
    if inp==[0,0,0,0,0,1,0,1]:
        b_8bit = safe_8bit
        #do nothing
            
    return [a_8bit, b_8bit]

def complement_8bit(n_8bit):
    catch_error(n_8bit, message="completment_8bit")

    
    out = [n ^ 1 for n in n_8bit]
    return add_8bit(out, [0]*8, carry=1)[0] #ohne carry

def catch_error(inp, inp_typ=list, length=8,  message=""):
    if not isinstance(inp, inp_typ): raise TypeError("TypeError"+message)
    if inp_typ == list and len(inp) != length: raise TypeError("WrongLength"+message)

def player_inp_8bit(inp="Gebe eine 8bit Binär Zahl an: ")-> list[int]:
    bitstring = input(inp)
    if any(c not in "01" for c in bitstring):
        raise ValueError("Only 0 and 1 allowed")

    return [int(c) for c in bitstring]

def bin_to_dec(bits):
    return int("".join(str(b) for b in bits), 2)

class Ram:
    def __init__(self):
        self.data = [Safe_8bit() for _ in range(256)]

    def read(self, adress_8bit):
        return self.data[bin_to_dec(adress_8bit)].read()

    def write(self, adress_8bit, data):
        self.data[bin_to_dec(adress_8bit)].write(data)

class Cpu:
    def __init__(self, cnt, ram):
        self.cnt = cnt
        self.ram = ram
        self.inp_control = Safe_8bit()
        self.inp_data = Safe_8bit()
        self.data = Safe_8bit()

    def run(self):
        while self.ram.read(self.cnt.read()) != [0,0,0,0,0,0,0,0]:
            self.inp_control.write(self.ram.read(self.cnt.read()))
            self.cnt.tick()
            self.inp_data.write(self.ram.read(self.cnt.read()))
            self.cnt.tick()
            self.data.write(add_8bit(
                                     *control_unit(self.inp_control.read(),self.inp_data.read(),self.data.read())
                                 )[0])
            print(self.data.read())
