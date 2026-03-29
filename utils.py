def add_1bit(bit_1, bit_2, carry):
    out_1 = bit_1 ^ bit_2 ^ carry
    carryer = (bit_1 and bit_2) or (bit_2 and carry) or (bit_1 and carry)
    return [out_1, carryer]
    
def add_8bit(a_8bit, b_8bit, carry):
    out_8bit = []
    for a_i, b_i in zip(a_8bit, b_8bit):
        out, carry = add_1bit(a_i, b_i, carry)
        out_8bit.append(out)
    return [out_8bit, carry]
