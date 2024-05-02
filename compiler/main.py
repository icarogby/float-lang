from tokenizer import Scanner


def main():
    with open('compiler/test.ft', 'r') as file:
        flooatCode = file.read()

    scanner = Scanner(flooatCode)

    for i in scanner.getTokenStream():
        print(i)

    print('\nEverything is fine!')


if __name__ == '__main__':
    main()
