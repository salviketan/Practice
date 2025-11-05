def print_formatted(number):
    for i in range(1,number+1):

        space_char = len(bin(number)[2:])

        int_repr = str(i).rjust(space_char)
        oct_repr = oct(i)[2:].rjust(space_char)
        hex_repr = hex(i)[2:].upper().rjust(space_char)
        bin_repr = bin(i)[2:].rjust(space_char)

        print(int_repr, oct_repr, hex_repr, bin_repr)


def my_print_formatted(number):
    for i in range(1,number+1):

        space_char = len(bin(number).lstrip('0b'))

        int_repr = str(i).rjust(space_char)
        oct_repr = oct(i).lstrip('0o').rjust(space_char)
        hex_repr = hex(i).lstrip('0x').upper().rjust(space_char)
        bin_repr = bin(i).lstrip('0b').rjust(space_char)

        print(int_repr, oct_repr, hex_repr, bin_repr)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)