
def Input():
    numericLiteral: str = "ob1001_10101_00101"
    if(decintegerDigit(numericLiteral) or decintegerNonZeroDigit(numericLiteral) or bininteger(numericLiteral) or octinteger(numericLiteral) or hexinteger(numericLiteral) ):
        print()

def decintegerDigit(numericLiteral: str) -> bool:
        
    return False
    
def decintegerNonZeroDigit(numericLiteral: str) -> bool:
        
    return False

#Vincent
def bininteger(numericLiteral: str) -> bool:
        
    return False
    
def octinteger(numericLiteral: str) -> bool:
        
    return False
#Vincent

#Timothy(and floating point)    
def hexinteger(numericLiteral: str) -> bool:
    if numericLiteral[0:2].lower() != "0x":
        return False
    
    hex_part : numericLiteral[2:]

    if hex_part[-1] == "_":
        return False

    if '__' in hex_part:
        return False
        
    cleaned = hex_part.replace('_', '')
    if not all(c in '0123456789abcdefABCDEF' for c in cleaned):
        return False
        
    return true
    

    

