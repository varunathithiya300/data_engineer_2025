def formatString(n):
    for i in range(1, n, 1):
        width_of_binary_number = len(bin(n)) - 2

        decn = str(i).rjust(width_of_binary_number, " ")
        hexa = hex(i)[2:].upper().rjust(width_of_binary_number, " ")
        octa = oct(i)[2:].rjust(width_of_binary_number, " ")
        bina = bin(i)[2:].rjust(width_of_binary_number, " ")

        print(decn, octa, hexa, bina)

formatString(5)