from flooatLexer import Lexer
from flooatParser import Parser


def main():
    with open('c:\\Users\\icaro\\OneDrive\\Documentos\\GitHub\\flooat-lang\\compiler\\test.floo', 'r') as file:
        flooatCode = file.read()

    lexer = Lexer(flooatCode)
    parser = Parser(lexer.getTokens())

    pythonCode = parser.parse()

    print('Everything is fine!')

    # todo: trade exceptions


if __name__ == '__main__':
    main()
