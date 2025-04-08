code: str = "1 + 2"
code2 = "( 1 + 1 ) * 2"
code3: str = '5 * ( 1 * ( 2 + 2 ) + ( ( 1 ) ) )'
code4: str = '5 * ( 1 * ( 2 + 2 ) + ( ( 1 ) ) ) ; 1 + 2 ; 3 * 4 ; 5 + 6 ; 7 * 8 ; 9 + 6 ;'
code5: str = 'var a = 5 '
code6: str = 'var a = 5 ; var b = 6 ; var c = a + b ;'
code7: str = 'var a = 5 ; var b = 8 ; var c = a + b ; var d = a * b + c ;'
code8: str = 'var a = 5 ; var b = 6 ; if ( a > b ) { var c = a + b ; } else { var d = a * b + c ; }'


stack: dict = {}
splittedLines = code7.split(";")
completeTokens = [subarray.split() + [''] for subarray in splittedLines]

tokens = completeTokens[0]
codeLineNum = 0
parseProgress: int = 0


def parseTokens(number: int = 1):
    global tokens
    global parseProgress
    takenOut: str
    if parseProgress >= len(tokens):
        Exception("Invalid input in parseTokens function")
    if number == 1:
        takenOut = tokens[parseProgress]
    else:
        takenOut = tokens[parseProgress:(parseProgress + number)]
    parseProgress += number
    return takenOut


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
        if isinstance(self.value, int):
            return self.value
        elif isinstance(int(self.value), int):
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

def V():
    global tokens
    global parseProgress
    if tokens[parseProgress] == '':
        return
    elif tokens[parseProgress] == 'var':
        parseTokens()
        varName = parseTokens()
        if varName.isnumeric():
            raise Exception("Invalid variable name: Variable names cannot be numbers")
        if tokens[parseProgress] != '=':
            raise Exception("Invalid input in V function")
        parseTokens()
        resS = S()
        stack[varName] = resS.evaluate()
        # return Variable(varName, resS.evaluate())
    else:
        resS = S()
        print (resS.evaluate())

def A():
    global tokens
    global parseProgress
    resB = B()
    resA = A_(resB)
    return resA

def A_(lfs):
    global tokens
    global parseProgress
    match tokens[parseProgress]:
        case '*':
            parseProgress += 1
            resB = B()
            resA_ = A_(resB)
            return NodeTimes(lfs, resA_)
        case _:
            return lfs

def S():
    global tokens
    global parseProgress
    resA = A()
    resS = S_(resA)
    return resS

def S_(lfs):
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

def B():
    global tokens
    global parseProgress
    match   tokens[parseProgress]:
        case '(':
            parseTokens()
            resS = S()
            if tokens[parseProgress] != ')':
                Exception("Invalid input in B function")
            parseTokens()
            return resS
        case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            number = parseTokens()
            return Node(number, None, None)
        case str(varName):
            parseTokens()
            
            number = stack.get(varName) 
            return Node(number, None, None)
        case _:
            Exception("Invalid input in B function")
    # return Node(lfs[0], None, None)


def compile():
    global codeLineNum
    global completeTokens
    global parseProgress
    global tokens
    while codeLineNum < len(completeTokens):
        tokens = completeTokens[codeLineNum]
        codeLineNum += 1
        V()
        parseProgress = 0
        print(stack)
        # if isinstance(res, Node):
        #     print(res.evaluate())
        # elif isinstance(res, Variable):
        #     print(res.value)
        # else:
        #     Exception("Invalid input in compile function")



compile()


# gramatika = {
#     "V": ['var x =', 'S'],
#     "V.": S,
#     "S": ['A', 'S.'],
#     "S.": ['+', 'A', 'S.'],
#     'S.': [None],
#     "A": ['B', 'A.'],
#     "A.": ['*', 'B', 'A.'],
#     'A.': [None],
#     "B": ['(', 'S', ')'],
#     'B': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
# }
