from enum import Enum

stack: dict = {}  # stores variables

with open("code.txt", "r") as codeFile:
    code = codeFile.read().strip()  # Read the entire file and remove leading/trailing whitespace

splittedLines = code.split(';')
completeTokens = [subarray.split() + [''] for subarray in splittedLines]
tokens = completeTokens[0]
codeLineNum = 0
parseProgress: int = 0

'''used for choosing between > >= and == operators'''
class ComparisonOperator(Enum):
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
    EQUAL = "=="

'''Node with some value and left and right children inside a syntax tree '''
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
        if self.value == None:
            return None
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


class NodeCompare(Node):
    def __init__(self, left, right, comparison_type: ComparisonOperator):
        super().__init__(comparison_type, left, right)
        if not isinstance(comparison_type, ComparisonOperator):
            raise Exception("Invalid comparison operator type")

    def evaluate(self):
        left_value = self.left.evaluate()
        right_value = self.right.evaluate()

        match self.value:  # self.value holds the ComparisonOperator
            case ComparisonOperator.GREATER_THAN:
                return left_value > right_value
            case ComparisonOperator.GREATER_THAN_OR_EQUAL:
                return left_value >= right_value
            case ComparisonOperator.EQUAL:
                return left_value == right_value
            case _:
                raise Exception("Unsupported comparison operator")


def parseTokens(number: int = 1):
    global tokens
    global parseProgress
    takenOut: str
    if parseProgress >= len(tokens)-1:
        Exception("Invalid input in parseTokens function")
    if number == 1:
        takenOut = tokens[parseProgress]
    else:
        takenOut = tokens[parseProgress:(parseProgress + number)]
    parseProgress += number
    return takenOut


def moveToChar(char: str):
    global parseProgress
    global tokens
    if char == tokens[parseProgress]:
        parseProgress += 1
        print('incremented char so it finds the next one')
    while parseProgress < len(tokens) and tokens[parseProgress] != char:
        parseProgress += 1
    if parseProgress >= len(tokens):
        raise Exception(
            f"Invalid input in moveToChar function: '{char}' not found")
    return tokens[parseProgress]


def I():
    global tokens
    global parseProgress
    if tokens[parseProgress] == 'if':
        parseTokens()
        resC = C()
        if resC.evaluate():
            evaluate_if()
        else:
            evaluate_else()
    else:
        V()


def evaluate_if():
    if tokens[parseProgress-1] != '{':
        raise Exception('if statement body doesnt begin with {')
    resC = V()
    print(resC)


def evaluate_else():
    moveToChar('}')
    print(tokens[parseProgress])
    if tokens[parseProgress + 1] == 'else':
        parseTokens(3)
    resV = V()

# TODO - forbid assignin special chars as part of the varname


def V():
    global tokens
    global parseProgress
    if tokens[parseProgress] == 'var':
        parseTokens()
        varName = parseTokens()
        # or ['=', '==', '', '>', '>=' ].index(varName) >= 0 :
        if varName.isnumeric():
            raise Exception(
                "Invalid variable name: Variable names cannot be numbers ir special chars")
        if tokens[parseProgress] != '=':
            raise Exception("Invalid input in V function")
        parseTokens()
        resC = C()
        stack[varName] = resC.evaluate()
    elif tokens[parseProgress] == '':
        return
    elif stack.get(tokens[parseProgress]) is not None and tokens[parseProgress+1] == '=':
        varName = parseTokens()
        parseTokens()
        resC = C()
        if resC:
            stack[varName] = resC.evaluate()
    else:
        resC = C()
        if resC:
            print(resC.evaluate())


def C():
    global tokens
    global parseProgress
    resS = S()
    resC = C_(resS)
    return resC


def C_(lfs):
    global tokens
    global parseProgress
    operatorToken = parseTokens()
    if operatorToken == '==':
        resS = S()
        resC_ = C_(resS)
        return NodeCompare(lfs, resC_, ComparisonOperator.EQUAL)
    elif operatorToken == '>':
        resS = S()
        resC_ = C_(resS)
        return NodeCompare(lfs, resC_, ComparisonOperator.GREATER_THAN)
    elif operatorToken == '>=':
        resS = S()
        resC_ = C_(resS)
        return NodeCompare(lfs, resC_, ComparisonOperator.GREATER_THAN_OR_EQUAL)
    else:
        return lfs


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
            parseTokens()
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
        return NodeAdd(lfs, resS)
    else:
        return lfs


def B():
    global tokens
    global parseProgress
    match   tokens[parseProgress]:
        case ')':
            raise Exception("bracket begins with )")
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


def compile():
    global codeLineNum
    global completeTokens
    global parseProgress
    global tokens
    while codeLineNum < len(completeTokens):
        tokens = completeTokens[codeLineNum]
        codeLineNum += 1
        if len(tokens) == 1 and tokens[0] == '':
            parseProgress = 0
            continue
        I()
        parseProgress = 0
        print(stack)


compile()


# gramatika = {
#     "I": ['if', '{' 'C', I],
#     "I.": [ '}' V ],
#     "I.": [V],
#     "V": ['var x =', 'S'],
#     "V.": C,
#     "C": ['S', 'C.'],
#     "C.": ['c', S 'C.'],
#     "S": ['A', 'S.'],
#     "S.": ['+', 'A', 'S.'],
#     'S.': [None],
#     "A": ['B', 'A.'],
#     "A.": ['*', 'B', 'A.'],
#     'A.': [None],
#     "B": ['(', 'C', ')'],
#     'B': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
# }
