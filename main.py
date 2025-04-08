code:str = "1 + 2"
code2 = "( 1 + 1 ) * 2"
code3:str = '5 * ( 1 * ( 2 + 2 ) + ( ( 1 ) ) )'
code4:str = '5 * ( 1 * ( 2 + 2 ) + ( ( 1 ) ) ) ; 1 + 2 ; 3 * 4 ; 5 + 6 ; 7 * 8 ; 9 + 6 ;'

splittedLines = code4.split(";")
#tokens are added in the compile function
completeTokens = [subarray.split() + [''] for subarray in splittedLines]
tokens = completeTokens[0]
codeLineNum = 0
parseProgress:int = 0

def parseTokens(number:int=1):
    global tokens
    global parseProgress
    takenOut:str
    if parseProgress >= len(tokens):
        Exception("Invalid input in parseTokens function")
    if number ==1:
        takenOut = tokens[parseProgress]
    else:
      takenOut = tokens[parseProgress:(parseProgress +number)]
    parseProgress += number
    return takenOut

# class codeLines():
#     def __init__(self, tokens:str):
#         self.tokens =
#         self.codeLines = splitTokenLines(tokens)
        
#     def splitTokenLines(self):
#         return self.codeLines

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return self.__str__()
    
    def evaluate(self):
        if isinstance(int(self.value), int):
            return int(self.value)
        else:
            Exception("Invalid input for evaluation in Node class")

class NodeAdd(Node):
    def __init__(self, left, right):
        if not left or right:
            Exception("Invalid input for NodeAdd class")
        super().__init__('+', left, right)

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
    
class NodeTimes(Node):
    def __init__(self, left, right):
        super().__init__('*', left, right)

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


def A():
    global tokens
    global parseProgress
    # if parseProgress > len(tokens): # this shouldnt throw an error
    #     Exception("Invalid input in A function")
    # if tokens[parseProgress] != '':
    resB = B( )
    resA = A_(  resB)
    return resA
 

def A_(  lfs):
    global tokens
    global parseProgress
    match tokens[parseProgress]:
        case '*':
            parseProgress += 1
            resB = B(  )
            resA_ = A_(  resB)
            return NodeTimes(lfs, resA_)
        case _:
            return lfs

def S( ):
    global tokens
    global parseProgress
    resA = A( )
    resS = S_(resA)
    return resS
 
def S_( lfs):
    global tokens
    global parseProgress
    if tokens[parseProgress] == '+':
        parseTokens()
        resA = A()
        resS = S_(resA)
        return NodeAdd(lfs, resS,)
    else:
        return lfs
    # elif tokens[parseProgress] == '':
    #     return resA

def B( ):
    global tokens
    global parseProgress
    match   tokens[parseProgress]:
        case '(':
            parseTokens()
            resS = S()
            if tokens[parseProgress]!= ')':
                Exception("Invalid input in B function")
            parseTokens()
            return resS
        case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            number = parseTokens(1)
            return Node(number, None, None)
        case _:
            Exception("Invalid input in B function")
    # return Node(lfs[0], None, None)

def compile( ):
    global codeLineNum
    global completeTokens
    global parseProgress
    global tokens
    while codeLineNum < len(completeTokens)-1:
        tokens = completeTokens[codeLineNum]
        codeLineNum += 1
        res=S()
        parseProgress = 0
        if res:
           print(res.evaluate())
        else:
            Exception("Invalid input in compile function")
        
    return


compile( )



# gramatika = {

#     "S": ['A', 'S.'],
#     "S.": ['+', 'A', 'S.'],
#     'S.': [None],
#     "A": ['B', 'A.'],
#     "A.": ['*', 'B', 'A.'],
#     'A.': [None],
#     "B": ['(', 'S', ')'],
#     'B': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
# }
