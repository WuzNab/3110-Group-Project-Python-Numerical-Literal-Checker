#Ricky
def decintegerDigit(numericLiteral: str) -> bool:
        
    return False

#Ricky    
def decintegerNonZeroDigit(numericLiteral: str) -> bool:
        
    return False

#Vincent
def bininteger(numericLiteral: str) -> bool:
    if numericLiteral[:2].lower() != "0b":
        return False

    binary_part = numericLiteral[2:]

    if not binary_part:
        return False

    if binary_part[-1] == '_':
        return False

    if '__' in binary_part:
        return False
    
    cleaned = binary_part.replace('_', '')
    
    if not all(c in '01' for c in cleaned):
        return False
    
    return True
    
def octinteger(numericLiteral: str) -> bool:
    if numericLiteral[:2].lower() != "0o":
        return False

    octal_part = numericLiteral[2:]

    if not octal_part:
        return False
    
    if octal_part[-1] == '_':
        return False
    
    if '__' in octal_part:
        return False

    cleaned = octal_part.replace('_', '')
    if not all(c in '01234567' for c in cleaned):
        return False
    
    return True
#Vincent

#Timothy(and floating point)    
def hexinteger(numericLiteral: str) -> bool:
        
    return False

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
            if(decintegerDigit(numericLiteral) or decintegerNonZeroDigit(numericLiteral) or bininteger(numericLiteral) or octinteger(numericLiteral) or hexinteger(numericLiteral) ):
                Output(numericLiteral, True)
            else:
                Output(numericLiteral, False)
      
#begin
Input()
    

    

    

