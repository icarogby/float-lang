# Used by tokenizer.py
reversedWords = ['comp', 'and', 'or']
decimalAlphabet = [str(i) for i in range(10)] # 0-9
firstCharsIdAlphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + ['_'] # a-z, A-Z, _
idAlphabet = firstCharsIdAlphabet + decimalAlphabet # a-z, A-Z, _, 0-9

symbolAlphabet = ['=', '(', ')', ';', ',']
ignoredChars = ['\n', '\t', ' ']
tokenClosers = symbolAlphabet + ignoredChars
