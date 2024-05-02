from tokenizer import Tokenizer


def main():
    with open('compiler/test.ft', 'r') as file:
        flooatCode = file.read()

    tokenizer = Tokenizer(flooatCode)

    for i in tokenizer.getTokenStream():
        print(i)

    print('\nEverything is fine!')


if __name__ == '__main__':
    main()
