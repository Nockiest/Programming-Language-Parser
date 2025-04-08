code = "1+1"
code2 = "1+1*2"
code3 = "1+1*2+3"
code4 = "1+1*2+3*4"

gramatika = {
    "S": ['A', 'S.'],
    "S.": ['+', 'A', 'S.'],
    'S.': [None],
    "A": ['B', 'A.'],
    "A.": ['*', 'B', 'A.'],
    'A.': [None],
    "B": ['(', 'S', ')'],
    'B': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
}

#tokens are added in the compile function
tokens = []


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


def A(lfs: str):
    if lfs[0] == '': # this shouldnt throw an error
        Exception("Invalid input in A function")
    if lfs[0] != '':
        resB = B(lfs)
        resA = A_(lfs, resB)
        return resA
    else:
        Exception("Invalid input in A function")

def A_(lfs: str, resB):
    match lfs[0]:
        case '*':
            resB = B(lfs[1:])
            resA_ = A_(lfs[1:], resB)
            return NodeTimes(lfs , resA_)
        case None:
            Exception("Invalid input in A_ function")
        case _:
            return resB

def S( ):
    resA = A(lfs)
    resS = S_(lfs[:len(resA.value)], resA)
    return resS
 
def S_(lfs: str, resA):
    match lfs[0]:
        case '+':
            resA = A(lfs[1:])
            resS = S_(lfs[1:], resA)
            return resS
        case '':
            return resA
        case _:
            Exception("Invalid input in S function")
    
    return
    


def B(lfs: str):
    match lfs[0]:
        # case '(':
        #     resS = S(lfs[1:])
        #     if lfs[0] != ')':
        #         Exception("Invalid input in B function")
        #     return resS
        case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            return Node(int(lfs[0]), None, None)
        case _:
            Exception("Invalid input in B function")
    return Node(lfs[0], None, None)


def compile(code: str):
    print(code)
    tokens.append(code.split()) # wont work for n>1 digit numbers
    res = S()
    print(res)
    return


compile(code)
