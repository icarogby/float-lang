firstLetterIdAlphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + ['_']
idAlphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)] + ['_']
numberAlphabet = [str(i) for i in range(10)]
symbolAlphabet = ['=', '(', ')', '[', ']', '{', '}', ';', ',']
ignoredChars = ['\n', '\t', ' ']
tokenEnds = symbolAlphabet + ignoredChars

tokenLabels = ['keyword', 'id', 'number', 'binary']
keyWords = ['comp', 'and', 'or', 'xor', 'not', 'nand', 'nor', 'xnor']
signTypes = ['bit']
