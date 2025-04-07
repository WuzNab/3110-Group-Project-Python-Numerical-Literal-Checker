#Ricky
def decintegerDigit(numericLiteral: str) -> bool:
        
    return False

#Ricky    
def decintegerNonZeroDigit(numericLiteral: str) -> bool:
        
    return False

#Vincent
def bininteger(numericLiteral: str) -> bool:
    #takes the first 2 digits and checks if they are 0o
    if numericLiteral[:2].lower() != "0b":
        return False

    #takes digits after the first 2
    binary_part = numericLiteral[2:]

    #checks to see if it start with _
    if binary_part[-1] == '_':
        return False

    #checks to see if __
    if '__' in binary_part:
        return False
    
    cleaned = binary_part.replace('_', '')
    
    #removes all _ from string to check for digits
    if not all(c in '01' for c in cleaned):
        return False
    
    return True
    
def octinteger(numericLiteral: str) -> bool:
    #takes the first 2 digits and checks if they are 0o
    if numericLiteral[:2].lower() != "0o":
        return False

    #takes digits after the first 2
    octal_part = numericLiteral[2:]
    
    #checks to see if it start with _
    if octal_part[-1] == '_':
        return False
    
    #checks to see if __
    if '__' in octal_part:
        return False

    #removes all _ from string to check for digits
    cleaned = octal_part.replace('_', '')
    if not all(c in '01234567' for c in cleaned):
        return False
    
    return True
#Vincent

#Timothy(and floating point)    
def hexinteger(numericLiteral: str) -> bool:
    if numericLiteral[0:2].lower() != "0x":
        return False
    
    hex_part = numericLiteral[2:]

    if not hex_part:
        return False

    if hex_part[-1] == "_":
        return False

    if '__' in hex_part:
        return False
        

    cleaned = hex_part.replace('_', '')
    if not all(c in '0123456789abcdefABCDEF' for c in cleaned):
        return False
        
    return True

def floatingPoint(numericLiteral: str) -> bool:
    if not numericLiteral:
        return False

    if numericLiteral.lower().count('e') + numericLiteral.lower().count('E') > 1:
        return False

    if 'e' in numericLiteral or 'E' in numericLiteral:
        parts  = numericLiteral.split('e') if 'e' in numericLiteral else numericLiteral.split('E')
    
        if len(parts) != 2:
            return False

        base, exponent = parts

        if not exponent or exponent[-1] == '_' or '__' in exponent:
            return False

        cleaned_exponent = exponent.replace('_', '')

        # Check if the exponent is a valid integer, allowing for an optional sign ('+' or '-')
        # Now, we also check that there are digits after the sign
        if cleaned_exponent and cleaned_exponent.lstrip('-+').isdigit():
            return True  # Exponent is valid
        else:
            return False  # Exponent is invalid


    else :
        base = numericLiteral
        if base[-1] == '_' or '__' in base:
            return False

        if "." not in base:
            return False

        if base[-1] == "_":
            return False

        if "__" in base:
            return False

        cleaned_base = base.replace('_', '')
        if not all(c in '0123456789.' for c in cleaned_base):
            return False

        if cleaned_base.count('.') > 1:
            return False

        return True

def Output(numericLiteral: str, result: bool):
    with open("out.txt", "a") as file:
        file.write(f"{numericLiteral} | {result}\n")

def Input():

    open("out.txt", "w")

    with open("in.txt", "r") as file:
        # Read each line from the file
        for line in file:
            # Remove any leading/trailing whitespace including newlines
            numericLiteral = line.strip()

            #checks to see if numeric literal is null
            if not numericLiteral:
                Output(numericLiteral, False)

            if(decintegerDigit(numericLiteral) or decintegerNonZeroDigit(numericLiteral) or bininteger(numericLiteral) or octinteger(numericLiteral) or hexinteger(numericLiteral) or floatingPoint(numericLiteral) ):
                Output(numericLiteral, True)
            else:
                Output(numericLiteral, False)
      
#begin
Input()
    
    