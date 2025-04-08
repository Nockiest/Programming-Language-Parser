code:str = "1 + 1"
code2 = "1 + 1 * 2"
 
#tokens are added in the compile function
tokens = code2.split()
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

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return self.__str__()

class NodeAdd(Node):
    def __init__(self, left, right):
        super().__init__('+', left, right)

    def get_value(self):
        return self.left.get_value() + self.right.get_value()

class NodeTimes(Node):
    def __init__(self, left, right):
        super().__init__('*', left, right)

    def get_value(self):
        return self.left.get_value() * self.right.get_value()


def A():
    global tokens
    global parseProgress
    if tokens[parseProgress] == '' or  parseProgress > len(tokens): # this shouldnt throw an error
        Exception("Invalid input in A function")
    if tokens[parseProgress] != '':
        resB = B( )
        resA = A_(  resB)
        return resA
    else:
        Exception("Invalid input in A function")

def A_(  resB):
    global tokens
    global parseProgress
    if parseProgress >= len(tokens):
        return resB
    match tokens[parseProgress]:
        case '*':
            parseProgress += 1
            resB = B(  )
            resA_ = A_(  resB)
            return NodeTimes(resB, resA_)
        case None:
            Exception("Invalid input in A_ function")
        case _:
            return resB

def S( ):
    global tokens
    global parseProgress
    resA = A( )
    resS = S_(resA)
    return resS
 
def S_( resA):
    global tokens
    global parseProgress
    if parseProgress >= len(tokens):
        return resA
    elif tokens[parseProgress] == '+':
        parseTokens()
        resA = A()
        resS = S_(resA)
        return NodeAdd(resS, resA)
    # elif tokens[parseProgress] == '':
    #     return resA
    else:
        Exception("Invalid input in S function")
    return
    


def B( ):
    global tokens
    global parseProgress
    match   tokens[parseProgress]:
        # case '(':
        #     resS = S()
        #     if lfs[0] != ')':
        #         Exception("Invalid input in B function")
        #     return resS
        case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            number = parseTokens(1)
            return Node(number, None, None)
        case _:
            Exception("Invalid input in B function")
    # return Node(lfs[0], None, None)


def compile(code: str):
    print(code)
    res = S()
    print(res)
    return


compile(code)



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
