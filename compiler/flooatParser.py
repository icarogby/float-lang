from util import tokenLabels

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.symbolTable = []
        self.pythonCode = ''
        self.index = -1
        self.expectedTokens = []
        self.SyntaxErrorMsg = f'Syntax error: Expected {list(set(self.expectedTokens))}.\n Found: {self.getCurrentToken()[0]}'

    def getCurrentToken(self):
        return self.tokens[self.index]
    
    def getNextToken(self):
        self.index += 1
        return self.tokens[self.index]
    
    def peekNextToken(self):
        return self.tokens[self.index + 1]
    
    def matchToken(self, token: str):
        if self.getNextToken()[0] != token:
            self.expectedTokens.append(token)
            raise Exception(self.SyntaxErrorMsg)
        
    def tryEnter(self, func, firstSet):
        if self.peekNextToken()[0] in firstSet:
            func()
        else:
            for token in firstSet:
                self.expectedTokens.append(token)

    def init(self):
        self.comp()

    def comp(self):
        self.matchToken('comp')

        self.matchToken('id')
        self.symbolTable.append(self.tokens[self.index][1])
        
        self.matchToken('[')
        
        self.tryEnter(self.parameters(), ['bit'])

        self.matchToken(']')
        
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
