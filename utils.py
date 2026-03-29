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
