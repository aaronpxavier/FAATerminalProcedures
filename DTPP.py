#/usr/bin/env

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
        #try catch ensures getChartData() method returns valid binary data.
        try:
            file.write(chart.getChartData())
        except Exception:
            print ("could not download chart " + chart.getChartName())
        file.close()
        os.chdir(directory)


def main():
    root_directory = os.getcwd()
    ARG_LENGTH = len(sys.argv)
    chartsArry = []
    if ARG_LENGTH < 2:
        printUsage()
        return

    for i in range(1, ARG_LENGTH):
        argument = sys.argv[i]
        if os.path.isdir(argument):
            if (ARG_LENGTH - 1 == i and ARG_LENGTH > 2):
                root_directory = argument
            elif (ARG_LENGTH == 2):
                printUsage()
            else:
                print("Invalid - directory must be last argument")
                return
        elif len(argument) == 3 or len(argument) == 4:
            scraper = DTPPScraper(argument)
            scraper.downloadCharts()
            try:
                chartsArry.extend(scraper.getCharts())
            except Exception:
                print("no charts found for id " + argument)
        else:
            print("arguments must be valid 3 or 4 letter aiprort id")

    writeChartsToDirectory(chartsArry,root_directory)

if __name__ == "__main__":
    main()