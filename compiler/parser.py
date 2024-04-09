class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.symbolTable = []
        self.pythonCode = ''

    def getNextToken(self):
        return self.tokens.pop(0)

    def init(self):
        if self.getNextToken()[1] != 'comp':
            raise Exception('Expected "comp"')
        else:
            print('OK')

