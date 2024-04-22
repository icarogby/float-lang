from util import *  # todo: change here


def getLabel(token: str):
    if token in keyWords: # Check if is a keyword
        return (token, token)

    elif token in signTypes: # Check if is a sign type
        return ('signType', token)
    
    elif (token[0] in firstLetterIdAlphabet) and (all(i in idAlphabet for i in token[1:])): # Check if is an ID
        return ('id', token)
    
    elif all(i in numberAlphabet for i in token): # Check if is a number
        return ('number', token)
    
    elif (token[0] == '\"') and (all(i in ['0', '1'] for i in token[1::-2])) and (token[-1] == '\"'): # Check if is a binary
        return ('binary', token)
    
    else:
        raise Exception(f'Lexical Error: Invalid token: {token}')
    

class Scanner:
    def __init__(self, flooatCode: str):
        self.tokenStream = []

        self.makeTokenStream(flooatCode)

    def makeTokenStream(self, flooatCode: str) -> list[tuple]:
        tempToken = ''
        reading = False

        for char in flooatCode:
            if reading:
                if char in tokenEnds:
                    reading = False

                    self.tokens.append(getLabel(tempToken))
                    tempToken = ''

                    if char in symbolAlphabet:
                        self.tokens.append((char, char))
                else:
                    tempToken += char

            else:
                if char in ignoredChars:
                    continue
                elif char in symbolAlphabet:
                    self.tokens.append((char, char))
                else:
                    reading = True
                    tempToken += char

    def getTokenStream(self):
        return self.tokens
