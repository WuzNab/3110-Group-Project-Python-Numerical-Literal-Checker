
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

    if numericLiteral.lower().count('e' > 1) :
        return False

    if 'e' in numericLiteral or 'E' in numericLiteral:
        parts  = numericLiteral.split('e') if 'e' in numericLiteral else numericLiteral.split('E')
    
        if len(parts) != 2:
            return False

        base, exponent = parts

        if not exponent or exponent[-1] == '_' or '__' in exponent:
            return False

        cleaned_exponent = exponent.replace('_', '')
        if not cleaned_exponent.lstrip('-').isdigit():
            return False

    else :
        base = numericLiteral
        if base[-1] == '_' or '__' in base:
            return False

        if "." not in base:
            return False

        if base[-1] == "_" or base[-1] ==  ".":
            return False

        if "__" in base:
            return False

        cleaned_base = base.replace('_', '')
        if not all(c in '0123456789.' for c in cleaned_base):
            return False

        if cleaned_base.count('.') > 1:
            return False

        return True


    

