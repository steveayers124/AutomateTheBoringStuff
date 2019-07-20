#! python3
# Given a list of a list of strings, each inner list having the same number of items,
# display all this in a well-organized table, having each column right-justified.
# Example:
# tableData = [['apples', 'oranges', 'cherries', 'bananas'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dog', 'cat', 'moose', 'goose']]

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dog', 'cat', 'moose', 'goose']]


def printTable(listOfLists):
    if tableData != []:
        # rowCount = len(tableData)
        if tableData[0] != []:
            # colCount = len(tableData[0])
            colWidth = []
            printTableLine = []
            for j in range(len(tableData[0])):
                colWidth += [0]
            for i in range(len(tableData)):
                for j in range(len(tableData[i])):
                    if len(tableData[i][j]) > colWidth[j]:
                        colWidth[j] = len(tableData[i][j])
                printTableLine += ['']
            for i in range(len(tableData)):
                for j in range(len(tableData[i])):
                    printTableLine[i] += tableData[i][j].rjust(colWidth[j]) + ' '
            for i in range(len(printTableLine)):
                print(printTableLine[i])


printTable(tableData)
