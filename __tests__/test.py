import unittest
from ..main import compile, completeTokens, code, code2, code3, code4, code5, code6

class TestCompiler(unittest.TestCase):
    def setUp(self):
        # Reset global variables before each test
        global completeTokens, codeLineNum, parseProgress, tokens
        codeLineNum = 0
        parseProgress = 0

    def test_simple_addition(self):
        global completeTokens
        completeTokens = [code.split()]
        with self.assertLogs() as log:
            compile()
        self.assertIn("3", log.output[0])  # 1 + 2 = 3

    def test_parentheses_and_multiplication(self):
        global completeTokens
        completeTokens = [code2.split()]
        with self.assertLogs() as log:
            compile()
        self.assertIn("4", log.output[0])  # (1 + 1) * 2 = 4

    def test_nested_parentheses(self):
        global completeTokens
        completeTokens = [code3.split()]
        with self.assertLogs() as log:
            compile()
        self.assertIn("20", log.output[0])  # 5 * (1 * (2 + 2) + ((1))) = 20

    def test_multiple_expressions(self):
        global completeTokens
        completeTokens = [line.split() + [''] for line in code4.split(";")]
        with self.assertLogs() as log:
            compile()
        self.assertIn("20", log.output[0])  # First expression: 5 * (1 * (2 + 2) + ((1))) = 20
        self.assertIn("3", log.output[1])   # Second expression: 1 + 2 = 3
        self.assertIn("12", log.output[2])  # Third expression: 3 * 4 = 12

    def test_variable_assignment(self):
        global completeTokens
        completeTokens = [line.split() + [''] for line in code6.split(";")]
        with self.assertLogs() as log:
            compile()
        self.assertIn("11", log.output[2])  # var c = a + b; a = 5, b = 6, c = 11

if __name__ == "__main__":
    unittest.main()