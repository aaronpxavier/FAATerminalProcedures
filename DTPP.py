
import sys
import os
from DTPPScraper import Scraper

def main():
    rootDirectory = os.getcwd()
    argLength = len(sys.argv)
    scraper = Scraper()
    currntCycl = scraper.getCurrentCycl()
    if argLength < 2:
        print("Usage - \"./scraper KJFK KLAX MIA\"\n or  ./scraper KJFK JLAX /somedirectory")

    for i in range(1, argLength):
        argument = sys.argv[i]
        if (os.path.isdir(argument)):
            rootDirectory = argument
        elif (len(argument) == 3 or len(argument) == 4):
            scraper.parse(sys.argv[i])
        else:
            print("arguments must be 3 or 4 letter aiprort id")


if __name__ == "__main__":
    main()

