from scanner import Scanner


def main():
    with open('test.ft', 'r') as file:
        flooatCode = file.read()

    scanner = Scanner(flooatCode)

    print('Everything is fine!')


if __name__ == '__main__':
    main()
