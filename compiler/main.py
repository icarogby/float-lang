from lexer import Lexer
from parser import Parser

def main():
    with open('../incrementor.floo', 'r') as file:
        flooatCode = file.read()

    lexer = Lexer(flooatCode)
    parser = Parser(lexer.getTokens())

    parser.init()


if __name__ == '__main__':
    main()