
def consoleInput():
    numericLiteral = input("Enter Numerical Literal(s):")

    numericLiteralSwitchCase(numericLiteral)
    
def numericLiteralSwitchCase(numericLiteral: str):
    if decintegerDigit(numericLiteral):
        print()
    elif decintegerNonZeroDigit(numericLiteral):
        print()
    elif bininteger(numericLiteral):
        print()
    elif octinteger(numericLiteral):
        print()
    elif hexinteger(numericLiteral):
        print()
    
class FloatingPoints:
    print()

class IntegerLiterals:
    def decintegerDigit(numericLiteral: str) -> bool:
        
        return False
    
    def decintegerNonZeroDigit(numericLiteral: str) -> bool:
        
        return False

    def bininteger(numericLiteral: str) -> bool:
        
        return False
    
    def octinteger(numericLiteral: str) -> bool:
        
        return False
    
    def hexinteger(numericLiteral: str) -> bool:
        
        return False
    

    

