firstLetterIdAlphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + ['_']
idAlphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)] + ['_']
numberAlphabet = [str(i) for i in range(10)]
symbolAlphabet = ['=', '(', ')', '[', ']', '{', '}', ';', ',']
ignoredChars = ['\n', '\t', ' ']
tokenEnds = symbolAlphabet + ignoredChars

keyWords = ['comp', 'bit', 'and', 'or', 'xor', 'not', 'nand', 'nor', 'xnor']


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
        raise Exception(f'Invalid token: {token}')
