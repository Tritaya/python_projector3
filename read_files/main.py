

if __name__ == '__main__':
    print('Hello Word!')

    file = open('hello.txt',mode= 'w')

    file.write('Hello Wordl!')

    file.close()

    print(file)