#/usr/bin/env python

import sys
import os
from DTPPScraper import DTPPScraper


def printUsage():
    print("Usage - \"./scraper KJFK KLAX MIA KORD\"\n or  ./scraper KJFK KLAX /somedirectory")

def main():
    rootDirectory = os.getcwd()
    argLength = len(sys.argv)
    scraper = DTPPScraper()

    if argLength < 2:
        printUsage()
        return

    for i in range(1, argLength):
        argument = sys.argv[i]
        if os.path.isdir(argument):
            if (argLength - 1 == i and argLength > 2):
                rootDirectory = argument
            elif (argLength == 2):
                printUsage()
            else:
                print("Invalid - directory must be last argument")
                return
        elif len(argument) == 3 or len(argument) == 4:
            scraper.scrape(sys.argv[i])
        else:
            print("arguments must be valid 3 or 4 letter aiprort id")

if __name__ == "__main__":
    main()

