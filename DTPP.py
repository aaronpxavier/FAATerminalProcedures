#/usr/bin/env

import sys
import os
from DTPPScraper import DTPPScraper

#pre: fn takes no arguments
#post: prints error message.
def print_usg():
    print("Usage - \"./DTPP KJFK KLAX MIA KORD\"\n or  \"./DTPP KJFK KLAX /somedirectory\"")

#pre: charts_arry must be declared and defined with valid arry of Chart() objs.
#     directory must be declared and defined with valid directory string.
#post:pdf files contained in chart objs are written to passed in directory.
def write_chrts_to_dir(charts_arry, directory):
    os.chdir(directory)
    if not os.path.exists("Charts"): # if Charts directory doesn't exist inside root directory it is created
        os.makedirs("Charts")

    # loop writes pdf files inside Charts directory and creates sub directories as needed to organize charts.
    for chart in charts_arry:
        os.chdir("Charts")
        if not os.path.exists(chart.get_airport_id()):
            os.makedirs(chart.get_airport_id())
        os.chdir(chart.get_airport_id())
        if not os.path.exists(chart.get_procedure_name()):
            os.makedirs(chart.get_procedure_name())
        os.chdir(chart.get_procedure_name())
        file = open(chart.get_chart_name(), "wb")
        #try catch ensures get_chart_data() method returns valid binary data.
        try:
            file.write(chart.get_chart_data())
        except Exception:
            print ("could not download chart " + chart.get_chart_name())
        file.close()
        os.chdir(directory)


def main():
    root_directory = os.getcwd()
    ARG_LENGTH = len(sys.argv)
    charts_arry = []

    if ARG_LENGTH < 2:  #program requires arguments to be passed in to continue.
        print_usg()
        return

    for i in range(1, ARG_LENGTH):
        argument = sys.argv[i]
        if os.path.isdir(argument):
            if (ARG_LENGTH - 1 == i and ARG_LENGTH > 2): #logic statements check for proper use of directory argument
                root_directory = argument
            elif (ARG_LENGTH == 2):
                print_usg()
            else:
                print("Invalid - directory must be last argument")
                return
        elif len(argument) == 3 or len(argument) == 4:
            scraper = DTPPScraper(argument)
            scraper.download_charts()
            try:
                charts_arry.extend(scraper.get_charts())
            except Exception:
                print("no charts found for id " + argument)
        else:
            print("arguments must be valid 3 or 4 letter aiprort id")

    write_chrts_to_dir(charts_arry, root_directory)

if __name__ == "__main__":
    main()