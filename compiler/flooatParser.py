from util import tokenLabels

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.symbolTable = []
        self.pythonCode = ''
        self.index = -1
        self.bkpIndex = 0
        self.tempMsgError = ''

    def getNextToken(self):
        self.index += 1
        return self.tokens[self.index]
    
    def peekNextToken(self):
        return self.tokens[self.index + 1]
    
    def matchToken(self, token: str):
        if self.getNextToken()[0] != token:
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "{token}"')

    def init(self):
        self.comp()

    def comp(self):
        self.matchToken('comp')

        self.matchToken('id')
        self.symbolTable.append(self.tokens[self.index][1])
        
        if self.getNextToken()[1] != '(':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "("')
        
        if self.peekNextToken()[1] == 'bit':
            self.parameters()
        elif self.peekNextToken()[1] != ')':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "bit" or ")"')

        if self.getNextToken()[1] != ')':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected ")"')
        
        if self.getNextToken()[1] != '(':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "("')
        
        if self.peekNextToken()[1] == 'bit':
            self.parameters()
        elif self.peekNextToken()[1] != ')':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "bit" or ")"')

        if self.getNextToken()[1] != ')':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected ")"')
        
        if self.getNextToken()[1] != '{':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "{{"')

        if self.getNextToken()[1] != '}':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "}}"')
        
    def parameters(self):
        if self.getNextToken()[1] != 'bit':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "bit"')
            
        if self.getNextToken()[0] != 'id':
            raise Exception(f'{self.tempMsgError}Syntax error: Expected "ID"')
        
        if self.peekNextToken()[1] == ',':
            self.getNextToken()
            self.parameters()
