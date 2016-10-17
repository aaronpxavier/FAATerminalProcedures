#/usr/bin/env

import sys
import os
from DTPPScraper import DTPPScraper


def printUsage():
    print("Usage - \"./DTPP KJFK KLAX MIA KORD\"\n or  \"./DTPP KJFK KLAX /somedirectory\"")

#pre: charts_arry must be declared and defined with valid arry of Chart() objs.
#     directory must be declared and defined with valid directory string.
#post:pdf files contained in chart objs are written to passed in directory.
def writeChartsToDirectory(charts_arry, directory):
    os.chdir(directory)
    if not os.path.exists("Charts"): # if Charts directory doesn't exist in root directory it is created
        os.makedirs("Charts")

    # loop writes pdf files inside Charts directory and creates sub directories as needed to organize charts.
    for chart in charts_arry:
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
    charts_arry = []

    if ARG_LENGTH < 2:  #program requires arguments to be passed in to continue.
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
                charts_arry.extend(scraper.getCharts())
            except Exception:
                print("no charts found for id " + argument)
        else:
            print("arguments must be valid 3 or 4 letter aiprort id")

    writeChartsToDirectory(charts_arry,root_directory)

if __name__ == "__main__":
    main()