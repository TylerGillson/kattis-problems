import sys

octal = sys.stdin.readline().strip()
hexadecimal = str(hex(int(octal,8))).upper()[2::]
print(hexadecimal)

def oct_to_bin(x):
    return {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }[x]

def bin_to_hex(x):
    return {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }[x]

def quadinate(quads, binary):
    length = len(binary)
    if length < 4:
        #if '1' in binary:
        new_quad = '0'*(4-length) + binary
        quads.insert(0,new_quad)
        return quads
    quad = binary[length-4::]
    binary = binary[:length-4:]
    quads.insert(0,quad)
    return quadinate(quads, binary)

def octal_to_hexadecimal(octal):
    binary = ''.join([oct_to_bin(x) for x in octal])
    quads = []
    quadinate(quads, binary)
    hexadecimal = ''.join([bin_to_hex(x) for x in quads])
    if hexadecimal.count('0') == len(hexadecimal):
        hexadecimal = '0'
    else:    
        while hexadecimal[0]=='0':
            hexadecimal = hexadecimal[1::]
    return hexadecimal

#octal = sys.stdin.readline().strip()
#hexadecimal = octal_to_hexadecimal(octal)
#print(hexadecimal)