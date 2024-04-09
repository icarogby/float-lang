from util import *  # todo: change here


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
