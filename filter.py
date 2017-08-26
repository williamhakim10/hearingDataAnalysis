import csv
import sys
import argparse as ap

parser = ap.ArgumentParser('Filter a CSV')
parser.add_argument('inFile', help='File to be filtered')
parser.add_argument('-f', '--filter', metavar='PHRASE', nargs='+', default=[], help='List of words and phrases to search for, and remove resulting sentences from output CSV')
parser.add_argument('-H', '--highlight', metavar='PHRASE', nargs='+', help='List of words and phrases to search for, and highlight resulting sentences in output CSV')
args = parser.parse_args()

outputFile = open('filtered-' + args.inFile, 'w')
outputWriter = csv.writer(outputFile)

filteredCells, highlightedCells = 0, 0

with open(args.inFile, 'r') as csv_file:
     for row in csv.reader(csv_file):
          newRow = []
          for col in row:
               if all(x not in col for x in args.filter):
                    if args.highlight and any(y in col for y in args.highlight):
                         newRow.append(col.upper())
                         highlightedCells += 1
                    else:
                         newRow.append(col)
               else:
                    filteredCells += 1 
          outputWriter.writerow(newRow)

outputFile.close()
print 'Filtered out {} cells!\nHighlighted {} cells!'.format(filteredCells, highlightedCells)

    
