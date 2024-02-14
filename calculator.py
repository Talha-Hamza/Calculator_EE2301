from binary_fractions import Binary, TwosComplement

def split_binary(binary):
    # Split binary number into integer and fractional parts
    integer_part, _, fractional_part = binary.partition('.')
    return integer_part, fractional_part

# a function that takes any base and converts it to any other desired base
def convert(number, base, desired_base):
    # convert number to decimal first
    if base == 2:
        decimal = binary_decimal(number)
    elif base == 10:
        decimal = float(number)
    elif base == 16:
        decimal = hexadecimal_decimal(number)
    elif base == 8:
        decimal = octal_decimal(number)
    else:
        print("Invalid base")
        return
    
    # convert decimal to desired base
    if desired_base == 2:
        return decimal_binary(decimal)
    elif desired_base == 10:
        return decimal
    elif desired_base == 16:
        return decimal_hexadecimal(decimal)
    elif desired_base == 8:
        return decimal_octal(decimal)
    else:
        print("Invalid desired base")
        return


def binary_decimal(binary):
    integer_part, fractional_part = split_binary(binary)
    integer_part = int(integer_part, 2)
    fractional_part = sum(int(digit) / 2 ** (i + 1) for i, digit in enumerate(fractional_part))
    return integer_part + fractional_part

def binary_hexadecimal(binary):
    integer_part, fractional_part = split_binary(binary)
    integer_part = hex(int(integer_part, 2))[2:]
    fractional_part = ''.join(hex(int(digit, 2))[2:] for digit in fractional_part)
    return integer_part + '.' + fractional_part

def binary_octal(binary):
    integer_part, fractional_part = split_binary(binary)
    integer_part = oct(int(integer_part, 2))[2:]
    fractional_part = ''.join(oct(int(digit, 2))[2:] for digit in fractional_part)
    return integer_part + '.' + fractional_part

def decimal_binary(decimal):
    decimal = float(decimal)
    b = Binary(decimal)
    return b
def decimal_hexadecimal(decimal):
    decimal = float(decimal)  # Ensure decimal is converted to float before processing
    integer_part = int(decimal)
    fractional_part = decimal - integer_part
    hexadecimal_integer = ""
    while integer_part != 0:
        hexadecimal_integer = str(hex(integer_part % 16))[2:] + hexadecimal_integer
        integer_part = integer_part // 16
    hexadecimal_fractional = ""
    while fractional_part != 0:
        fractional_part *= 16
        digit = int(fractional_part)
        hexadecimal_fractional += str(hex(digit))[2:]
        fractional_part -= digit
    return hexadecimal_integer + "." + hexadecimal_fractional

def decimal_octal(decimal):
    decimal = float(decimal)  # Ensure decimal is converted to float before processing
    integer_part = int(decimal)
    fractional_part = decimal - integer_part
    octal_integer = ""
    while integer_part != 0:
        octal_integer = str(oct(integer_part % 8))[2:] + octal_integer
        integer_part = integer_part // 8
    octal_fractional = ""
    while fractional_part != 0:
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fractional += str(oct(digit))[2:]
        fractional_part -= digit
    return octal_integer + "." + octal_fractional

def hexadecimal_binary(hexadecimal):
    binary = ""
    if '.' not in hexadecimal:
        hexadecimal += '.0'
    decimal_part = int(hexadecimal.split('.')[0], 16)
    
    # Convert fractional part to binary without using float
    fractional_part = hexadecimal.split('.')[1]
    fractional_binary = ''.join(format(int(digit, 16), '04b') for digit in fractional_part)
    
    binary += bin(decimal_part)[2:]
    binary += "."
    binary += fractional_binary
    return binary

def hexadecimal_decimal(hexadecimal):
    if '.' not in hexadecimal:
        hexadecimal += '.0'
    integer_part = int(hexadecimal.split('.')[0], 16)
    
    # Convert fractional part to decimal without using float
    fractional_part = int(hexadecimal.split('.')[1], 16)
    fractional_decimal = fractional_part / (16 ** len(hexadecimal.split('.')[1]))
    
    return integer_part + fractional_decimal

def hexadecimal_octal(hexadecimal):
    decimal_number = float.fromhex(hexadecimal)
    decimal_integer = int(decimal_number)
    
    # Convert the integer part to octal
    octal_integer = oct(decimal_integer)[2:]
    
    # Extract the fractional part and convert it to octal
    fractional_part = decimal_number - decimal_integer
    fractional_octal = ""
    
    while fractional_part != 0:
        fractional_part *= 8
        digit = int(fractional_part)
        fractional_octal += str(digit)
        fractional_part -= digit
    
    return octal_integer + "." + fractional_octal



def octal_binary(octal):
    binary = ""
    if '.' not in octal:
        octal += '.0'
    decimal_part = int(octal.split('.')[0], 8)
    
    # Convert fractional part to binary without using float
    fractional_part = octal.split('.')[1]
    fractional_binary = ''.join(format(int(digit, 8), '03b') for digit in fractional_part)
    
    binary += bin(decimal_part)[2:]
    binary += "."
    binary += fractional_binary
    return binary

def octal_decimal(octal):
    if '.' not in octal:
        octal += '.0'
    integer_part = int(octal.split('.')[0], 8)
    
    # Convert fractional part to decimal without using float
    fractional_part = int(octal.split('.')[1], 8)
    fractional_decimal = fractional_part / (8 ** len(octal.split('.')[1]))
    
    return integer_part + fractional_decimal

def octal_hexadecimal(octal):
    # Convert octal to decimal, taking care of integer and fractional parts as decimal point may or may not be present
    # check if decimal point is present
    if '.' not in octal:
        octal += '.0'
    
    integer_part = int(octal.split('.')[0], 8)
    fractional_part = int(octal.split('.')[1], 8) / (8 ** len(octal.split('.')[1]))
    
    # Convert decimal part to hexadecimal
    integer_hexadecimal = hex(integer_part)[2:]
    
    # Convert fractional part to hexadecimal
    fractional_hexadecimal = ""
    while fractional_part != 0:
        fractional_part *= 16
        digit = int(fractional_part)
        fractional_hexadecimal += format(digit, 'x')
        fractional_part -= digit
        
    hexadecimal_result = f"{integer_hexadecimal}.{fractional_hexadecimal}"
    return hexadecimal_result


def twos_compliment(binary):
    # find two's complement of binary number=
    binary = list(binary)
    for i in range(len(binary)):
        if binary[i] == "0":
            binary[i] = "1"
        else:
            binary[i] = "0"
    binary = "".join(binary)
    # add 1 to the one's compliment
    binary = list(binary)
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == "0":
            binary[i] = "1"
            break
        else:
            binary[i] = "0"
    binary = "".join(binary)
    
    # return as many bits as the original binary number
    for i in range(len(binary)):
        if binary[i] == ".":
            binary = binary[:i]
            break
    return binary


def ones_compliment(binary):
    # find one's compliment of binary number like above
    binary = list(binary)
    for i in range(len(binary)):
        if binary[i] == "0":
            binary[i] = "1"
        else:
            binary[i] = "0"
    binary = "".join(binary)
    # return as many bits as the original binary number
    for i in range(len(binary)):
        if binary[i] == ".":
            binary = binary[:i]
            break
    return binary


def binary_addition(num1, num2):
    res = bin(int(num1, 2) + int(num2, 2))
    print(f"The sum is: {res}")
   

def binary_subtraction(num1, num2):
    res = bin(int(num1, 2) - int(num2, 2))
    print(f"The difference is: {res}")
    
def binary_multiplication(num1, num2):
    res = bin(int(num1, 2) * int(num2, 2))
    print(f"The product is: {res}")

def binary_division(num1, num2):
    res = bin(int(num1, 2) // int(num2, 2))
    print(f"The quotient is: {res}")
    

def main():
    while True:
        print("\n----------------------------------------------------")
        print("Choose an operation:")
        print("1. Conversion")
        print("2. Two's Complement")
        print("3. One's Complement")
        print("4. Binary Arithmetic")
        print("5. Exit\n")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        print('\n')

        if choice == '1':
            print('----------------------------------------------------\n')
            print("What is the base of the number you want to convert?")
            print("1. Binary")
            print("2. Decimal")
            print("3. Hexadecimal")
            print("4. Octal\n")
            base = input("Enter choice XY, where X is base and Y is desired base: ")
            print('\n')
            
            if base == '11' or base == '22' or base == '33' or base == '44':
                print('Double check your input. Try again.\n')
            elif base == '12':
                print('Enter a binary number to convert to decimal:')
                binary = input()
                result = binary_decimal(binary)
                print(f"Decimal: {result}")
            elif base == '13':
                print('Enter a binary number to convert to hexadecimal:')
                binary = input()
                result = binary_hexadecimal(binary)
                print(f"Hexadeimal: {result}")
            elif base == '14':
                print('Enter a binary number to convert to octal:')
                binary = input()
                result = binary_octal(binary)
                print(f"Octal: {result}")
            elif base == '21':
                print('Enter a decimal number to convert to binary:')
                decimal = (input())
                result = (decimal_binary(decimal))
                print(f"Binary: {result}")
            elif base == '23':
                print('Enter a decimal number to convert to hexadecimal:')
                decimal = (input())
                result = decimal_hexadecimal(decimal)
                print(f"Hexadecimal: {result}")
            elif base == '24':
                print('Enter a decimal number to convert to octal:')
                decimal = (input())
                result = decimal_octal(decimal)
                print(f"Octal: {result}")
            elif base == '31':
                print('Enter a hexadecimal number to convert to binary:')
                hexadecimal = input()
                result = hexadecimal_binary(hexadecimal)
                print(f"Binary: {result}")
            elif base == '32':
                print('Enter a hexadecimal number to convert to decimal:')
                hexadecimal = input()
                result = hexadecimal_decimal(hexadecimal)
                print(f"Decimal: {result}")
            elif base == '34':
                print('Enter a hexadecimal number to convert to octal:')
                hexadecimal = input()
                result = hexadecimal_octal(hexadecimal)
                print(f"Octal: {result}")
            elif base == '41':
                print('Enter an octal number to convert to binary:')
                octal = input()
                result = octal_binary(octal)
                print(f"Binary: {result}")
            elif base == '42':
                print('Enter an octal number to convert to decimal:')
                octal = input()
                result = octal_decimal(octal)
                print(f"Decimal: {result}")
            elif base == '43':
                print('Enter an octal number to convert to hexadecimal:')
                octal = input()
                result = octal_hexadecimal(octal)
                print(f"Hexadecimal: {result}")
            else:
                print('Invalid input :(\n')
                
        elif choice == '2':
            #take input in binary type
            binary = input("Enter binary number for Two's compliment: ")
            print(binary.format())
            print("Two's compliment: ")
            print(twos_compliment(binary))
        elif choice == '3':
            binary = input("Enter binary number for One's compliment: ")
            print("One's compliment: ")
            print(ones_compliment(binary))
        elif choice == '4':
            print("What do you want to do?")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            operation = input("Enter choice (1/2/3/4): ")
            num1 = input("Enter first binary number: ")
            num2 = input("Enter second binary number: ")
            if operation == '1':
                binary_addition(num1, num2)
            elif operation == '2':
                binary_subtraction(num1, num2)
            elif operation == '3':
                binary_multiplication(num1, num2)
            elif operation == '4':
                binary_division(num1, num2)
            else:
                print("Invalid input")
        elif choice == '5':
            print("Goodbye!")
            return False
        else:
            print("Invalid input")
        
            
if __name__ == "__main__":
    
    while main():
        pass