#BOOKS PROJECT - WEEKS 1-3 - MAYA-SCHWARTZ
import sys
import csv
import re

def readFile(file, action):
    lines = []
    x = 0
    if action == 'authors’:
        x = 2
    try:
        with open(file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                lines.append(row[x])
        return lines
    except:
        print("Usage: Invalid file name", file=sys.stderr)
        sys.exit()

def takeLast(elem):
    return elem[-1]

def getOrder(lines, action, dir):
    if action == "books":
        lines.sort()
        if not dir:
            lines.reverse()
        return lines
    else:
        authors = []
        for author in lines:
            x = re.findall("[^0-9()\-\s]+", author)
            authors.append(x)
        authors.sort(key=takeLast)
        if not dir:
            authors.reverse()
        return authors

def printNames(lines, action):
    if action == 'books':
        for name in lines:
            print(name)
    else:
        for name in lines:
            printableName = ''
            for item in name:
                printableName += item + ' '
            print(printableName)

def checkExceptions(initials):
    if len(initials) < 3:
        print('Usage: Not enough arguments supplied', file=sys.stderr)
        sys.exit()
    elif initials[2] != 'authors' and initials[2] != 'books':
        print('Usage: Invalid action', file=sys.stderr)
        sys.exit()
    elif len(initials) == 4:
        if initials[3] != 'forward' and initials[3] != 'reverse':
            print('Usage: Invalid direction supplied', file=sys.stderr)
            sys.exit()
    elif len(initials) > 4:
        print('Usage: Too many arguments supplied', file=sys.stderr)
        sys.exit()

def main():
    checkExceptions(sys.argv)
    file = sys.argv[1]
    action = sys.argv[2]
    dir = True
    if len(sys.argv) > 3:
        direction = sys.argv[3]
        if direction == 'reverse':
            dir = False
    lines = readFile(file, action)
    lines = getOrder(lines, action, dir)
    printNames(lines, action)

if __name__ == "__main__":
    main()