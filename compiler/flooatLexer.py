from util import *  # todo: change here


def getLabel(token: str):
    if token in keyWords:
        return 'keyword'
    elif (token[0] in firstLetterIdAlphabet) and (all(i in idAlphabet for i in token[1:])):
        return 'id'
    elif all(i in numberAlphabet for i in token):
        return 'number'
    elif (token[0] == '\"') and (all(i in ['0', '1'] for i in token[1::-2])) and (token[-1] == '\"'):
        return 'binary'
    else:
        raise Exception(f'Lexical Error: Invalid token: {token}')
    

class Lexer:
    def __init__(self, flooatCode: str):
        self.tokens = []
        self.currentToken = None

        self.splitAndLabelTokens(flooatCode)

    def splitAndLabelTokens(self, flooatCode: str):
        tempToken = ''
        reading = False

        for char in flooatCode:
            if reading:
                if char in tokenEnds:
                    reading = False

                    self.tokens.append((getLabel(tempToken), tempToken))
                    tempToken = ''

                    if char in symbolAlphabet:
                        self.tokens.append(('symbol', char))
                else:
                    tempToken += char

            else:
                if char in ignoredChars:
                    continue
                elif char in symbolAlphabet:
                    self.tokens.append(('symbol', char))
                else:
                    reading = True
                    tempToken += char

    def getTokens(self):
        return self.tokens
