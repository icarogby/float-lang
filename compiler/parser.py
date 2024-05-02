class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.index = -1
        self.tempIndex = 0

        self.tempErrorMsg = ''

        self.pythonCode = ''

    def parse(self):
        try:
            self.init()
        except Exception as e:
            print(f'Error: {e}')
        return self.pythonCode
    
    def getCurrentToken(self):
        return self.tokens[self.index]
    
    def getNextToken(self):
        self.index += 1
        return self.tokens[self.index]
    
    def peekNextToken(self):
        return self.tokens[self.index + 1]
    
    def matchToken(self, token: str):
        if self.getNextToken()[0] != token:
            raise Exception(f'Syntax error: Expected "{token}"{self.tempErrorMsg}.\n')
        
    def tryEnter(self, func: callable):
        try:
            self.tempIndex = self.index
            func()
        except Exception as e:
            self.tempErrorMsg = f' or {func.__name__} ({e})'
            self.index = self.tempIndex
            
    def init(self):
        self.comp()

    def comp(self):
        self.matchToken('comp')

        self.matchToken('id')
   
        self.matchToken('(')
        
        self.tryEnter(self.parameters)

        self.matchToken(')')

        self.tempErrorMsg = ''

        self.matchToken('(')
        
        self.tryEnter(self.parameters)

        self.matchToken(')')

        self.tempErrorMsg = ''

        return True
        
    def parameters(self):
        self.matchToken('signType')
            
        self.matchToken('id')
        
        if self.peekNextToken()[0] == ',':
            self.getNextToken()
            self.parameters()
