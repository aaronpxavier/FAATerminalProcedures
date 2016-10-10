#/usr/bin/env python

import sys
import os
from DTPPScraper import DTPPScraper


def printUsage():
    print("Usage - \"./DTPP KJFK KLAX MIA KORD\"\n or  ./DTPP KJFK KLAX /somedirectory")

def writeChartsToDirectory(chartsArry, directory):
    os.chdir(directory)
    if not os.path.exists("Charts"):
        os.makedirs("Charts")

    for chart in chartsArry:
        os.chdir("Charts")
        if not os.path.exists(chart.getAirportID()):
            os.makedirs(chart.getAirportID())
        os.chdir(chart.getAirportID())
        if not os.path.exists(chart.getProcedureName()):
            os.makedirs(chart.getProcedureName())
        os.chdir(chart.getProcedureName())
        file = open(chart.getChartName(), "wb")
        file.write(chart.getChartData())
        file.close()
        os.chdir(directory)


def main():
    rootDirectory = os.getcwd()
    argLength = len(sys.argv)
    chartsArry = []
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
            scraper = DTPPScraper(argument)
            scraper.downloadCharts()
            chartsArry.extend(scraper.getCharts())
        else:
            print("arguments must be valid 3 or 4 letter aiprort id")

    writeChartsToDirectory(chartsArry,rootDirectory)

if __name__ == "__main__":
    main()

