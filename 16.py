import fileinput
import re

input = list([l.strip() for l in fileinput.input()][0])



# bits = [bin(int(x, 16))[2:] for x in input]
#

# there is probably a better way
lookup = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

# input = 'A0016C880162017C3686B18A3D4780'
bits = ''.join([lookup[x] for x in input])



def decode_packet(bits, versions = []):
    if re.match(r'^0*$', bits):
        return versions


    version = int(bits[:3], 2)
    versions.append(version)
    # sum_versions += version

    type = int(bits[3:6], 2)
    print('version:', version)
    print('type', type)

    if type == 4: # Literal value
        start = 6
        v = ''
        end = False
        while not end:
            b = bits[start:start + 5]
            print('b', b)

            if b[0] == '0':
                end = True
                v += b[1:]
            else:
                v += b[1:]
            start += 5

        print('literal value', int(v, 2))
        return decode_packet(bits[start:], versions)

    else: # operator
        start = 6
        length_type_id = bits[start]
        print('length_type_id', length_type_id)
        if length_type_id == '0': # 15 bits
            total_length = int(bits[start + 1: start + 1 + 15], 2)
            print('total_length', total_length)
            decode_packet(bits[start + 1 + 15: start + 1 + 15 + total_length], versions)
            return decode_packet(bits[start + 1 + 15 + total_length:], versions)

        else: # 11 bits
            subpackets = int(bits[start + 1:start + 1 + 11], 2)
            print('subpackets', subpackets)
            return decode_packet(bits[start + 1 + 11:], versions)


# def decode_n_subpackets(bits, n):
#     if n == 0:
#         return
#     else:
#         pass



sum_versions = 0
print(sum(decode_packet(bits)))
