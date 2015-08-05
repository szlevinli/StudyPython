#######################################
# take one or more filenames are arguments
# and print all the lines which are larger than 40 characters
#######################################


def readFiles(filenames):
    for f in filenames:
        for line in open(f, encoding='utf-8'):
            yield line


def grepLines(lines, length):
    return (line for line in lines if len(line) > length)


def printLines(lines):
    for line in lines:
        print(line, end='')


def main(fileNames, length):
    lines = readFiles(fileNames)
    lines2 = grepLines(lines, length)
    printLines(lines2)
