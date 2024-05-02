from util import reversedWords, decimalAlphabet, firstCharsIdAlphabet, idAlphabet, symbolAlphabet, ignoredChars, tokenClosers


def getToken(token: str): # todo: make create symbols
    if token in reversedWords: # Check if is a reversed word
        return (token.upper(), token)
    
    if token in symbolAlphabet: # Check if is a symbol
        match token:
            case '=':
                return ('EQ', token)
            case '(':
                return ('OP', token)
            case ')':
                return ('CP', token)
            case ';':
                return ('SC', token)
            case ',':
                return ('CM', token)
            case _:
                raise Exception(f'It is very unlikely that this error will be raised. If it is, please contact the developer. Token: {token}')
            
    elif (token[0] in firstCharsIdAlphabet) and (all(i in idAlphabet for i in token[1:])): # Check if is an ID
        return ('ID', token)
    
    elif all(i in decimalAlphabet for i in token): # Check if is a number
        return ('DEC', token)
    
    else:
        raise Exception(f'Lexical Error: Invalid token: {token}')
    

class Scanner:
    def __init__(self, flooatCode: str):
        self.tokenStream = [] # List of tokens

        self.makeTokenStream(flooatCode)

    def makeTokenStream(self, flooatCode: str) -> list[tuple]: # Make the token stream
        tempLexeme = '' # Temporary lexeme while reading
        isReading = False # If is reading a token that have more than one character

        for char in flooatCode:
            if isReading:
                if char in tokenClosers: # If the char is a token end,
                    isReading = False # stop reading,

                    self.tokenStream.append(getToken(tempLexeme)) # append the token to the token stream
                    tempLexeme = '' # and clear the temporary lexeme.

                    if char in symbolAlphabet: # If the char in tokenEnds is a symbol,
                        self.tokenStream.append(getToken(char)) # Append the token to the token stream.

                else:
                    tempLexeme += char # If the char is not a token end, append the char to the temporary lexeme.

            else:
                if char in ignoredChars:
                    continue
                
                elif char in symbolAlphabet:
                    self.tokenStream.append(getToken(char))
                
                else:
                    isReading = True
                    tempLexeme += char

        if isReading: # If the scanner is reading a token when the code ends,
            self.tokenStream.append(getToken(tempLexeme)) # append the token to the token stream.

        self.tokenStream.append(('EOF', '\0'))  # Append the EOF token

    def getTokenStream(self) -> list[tuple]:
        return self.tokenStream
