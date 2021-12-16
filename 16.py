import re


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


input = '005473C9244483004B001F79A9CE75FF9065446725685F1223600542661B7A9F4D001428C01D8C30C61210021F0663043A20042616C75868800BAC9CB59F4BC3A40232680220008542D89B114401886F1EA2DCF16CFE3BE6281060104B00C9994B83C13200AD3C0169B85FA7D3BE0A91356004824A32E6C94803A1D005E6701B2B49D76A1257EC7310C2015E7C0151006E0843F8D000086C4284910A47518CF7DD04380553C2F2D4BFEE67350DE2C9331FEFAFAD24CB282004F328C73F4E8B49C34AF094802B2B004E76762F9D9D8BA500653EEA4016CD802126B72D8F004C5F9975200C924B5065C00686467E58919F960C017F00466BB3B6B4B135D9DB5A5A93C2210050B32A9400A9497D524BEA660084EEA8EF600849E21EFB7C9F07E5C34C014C009067794BCC527794BCC424F12A67DCBC905C01B97BF8DE5ED9F7C865A4051F50024F9B9EAFA93ECE1A49A2C2E20128E4CA30037100042612C6F8B600084C1C8850BC400B8DAA01547197D6370BC8422C4A72051291E2A0803B0E2094D4BB5FDBEF6A0094F3CCC9A0002FD38E1350E7500C01A1006E3CC24884200C46389312C401F8551C63D4CC9D08035293FD6FCAFF1468B0056780A45D0C01498FBED0039925B82CCDCA7F4E20021A692CC012B00440010B8691761E0002190E21244C98EE0B0C0139297660B401A80002150E20A43C1006A0E44582A400C04A81CD994B9A1004BB1625D0648CE440E49DC402D8612BB6C9F5E97A5AC193F589A100505800ABCF5205138BD2EB527EA130008611167331AEA9B8BDCC4752B78165B39DAA1004C906740139EB0148D3CEC80662B801E60041015EE6006801364E007B801C003F1A801880350100BEC002A3000920E0079801CA00500046A800C0A001A73DFE9830059D29B5E8A51865777DCA1A2820040E4C7A49F88028B9F92DF80292E592B6B840'
# input = '9C0141080250320F1802104A08'


bits = ''.join([lookup[x] for x in input])

res = 0

versions = []

def decode_packet(bits, idx = 0):
    if re.match(r'^0*$', bits):
        return

    version = int(bits[idx: idx + 3], 2)
    versions.append(version)

    print('version:', version)

    type = int(bits[idx + 3: idx + 6], 2)
    print('type', type)

    parsed_idx = idx + 6

    if type == 4: # Literal value
        # curr_idx = idx + 6

        v = ''
        end = False
        while not end:
            b = bits[parsed_idx:parsed_idx + 5]
            print('b', b)

            if b[0] == '0':
                end = True
                v += b[1:]
            else:
                v += b[1:]
            parsed_idx += 5


        print('literal value', int(v, 2))
        return int(v, 2), parsed_idx
        # return decode_packet(bits[start_idx:], subvalues)

    else: # operator
        subvalues = []

        length_type_id = bits[parsed_idx]
        print('length_type_id', length_type_id)
        parsed_idx += 1

        if length_type_id == '0': # 15 bits
            total_length = int(bits[parsed_idx: parsed_idx + 15], 2)
            parsed_idx += 15

            print('total_length', total_length)

            end_idx = parsed_idx + total_length

            while parsed_idx < end_idx:
                v, parsed_idx = decode_packet(bits, parsed_idx)
                subvalues.append(v)

        else: # 11 bits
            subpackets = int(bits[parsed_idx: parsed_idx + 11], 2)
            print('# subpackets', subpackets)
            parsed_idx += 11

            for _ in range(subpackets):
                v, parsed_idx = decode_packet(bits, parsed_idx)
                subvalues.append(v)

        val = None
        if type == 0:
            val = sum(subvalues)
        elif type == 1:
            val = 1
            for s in subvalues:
                val *= s
        elif type == 2:
            val = min(subvalues)
        elif type == 3:
            val = max(subvalues)
        elif type == 5:
            val = 1 if subvalues[0] > subvalues[1] else 0
        elif type == 6:
            val = 1 if subvalues[0] < subvalues[1] else 0
        elif type == 7:
            val = 1 if subvalues[0] == subvalues[1] else 0
        else:
            print('error')

        return val, parsed_idx


print("part 2: ", decode_packet(bits)[0])
print("part 1: ", sum(versions))
