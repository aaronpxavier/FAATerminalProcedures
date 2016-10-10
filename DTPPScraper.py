#!/usr/bin/env

from __future__ import print_function
import urllib.request
import re
import datetime
from chart import Chart
from bs4 import BeautifulSoup

class DTPPScraper:

    # pre: identIn must be declared and defined with valid 3 or 4 character airport id.
    # post: stores scraped charts in charts[] attribute and creates new instance of DTPPScraper class
    def __init__(self, identIn):
        self.__ident = ""
        self.__charts = []
        pageCount = 0
        identGetParameter =  "&ident=" + identIn
        self.__ident = identIn
        baseurl = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/"
        cycle = self.getCurrentCycl()
        url = baseurl + cycle + identGetParameter

        # loops through html pages in FAA chart results. finishes when all pages have been scraped
        while (True):
            # gets html document from FAA chart results
            bSoup = BeautifulSoup(urllib.request.urlopen(url),"html.parser")

            # increment is used in http get request attribute to cycle thru pages
            pageCount += 1
            print ("Accessing charts for: " + identIn)
            print("scraping page " + url)
            # loads next page if tableRowtravers() returns true, breaks loop if tableRowtravers() returns false
            if (self.__tableRowTraverse(bSoup)):
                # creates new url for next page if there are more pages in result
                url = baseurl + cycle + identGetParameter + "&page=" + str(pageCount+1)
            else:
                break

    #pre:method takes no argument. Charts attribute must not be empty.
    #post:downloads pdf file for the last Chart object in Charts array.
    def downloadCharts(self):
        for chart in self.__charts:
            print("downloading " + chart.getChartName() +
              " from " + chart.getPDFURL())
            try:
                request = urllib.request.urlopen(chart.getPDFURL())
            except Exception:
                print("Could not download chart " + chart.getChartName())
            chart.setChartData(request.read())


    # traverses columns in page table
    # pre: tag must be declared and defined
    # post: traverses page table column. returns chart object.
    def __tableColumnTraverse(self,tag):
        self.__charts.append(Chart())
        for index, tag in enumerate(tag.find_all(re.compile("td"))):
            if index == 3 :
                airportID = tag.text
                if airportID[airportID.find("(")+1:airportID.find(")")] != "" :
                    self.__charts[-1].setAirportID(airportID[airportID.find("(") + 1:airportID.find(")")])
                else:
                    self.__charts[-1].setAirportID(airportID[:3])
            elif index == 4 :
                self.__charts[-1].setRegionName(tag.text)
            elif index == 6 :
                self.__charts[-1].setProcedureName(tag.text)
            elif index == 7 :
                if tag.a:
                    chartName = tag.text[:-6]+".pdf"
                    self.__charts[-1].setPDFURL(tag.a['href'])
                    self.__charts[-1].setChartName(chartName.replace("/", "_"))
        if self.__charts[-1].getPDFURL() == '':
            self.__charts.pop()


    # traverses all rows in page table.
    # pre: soup and cnx are defined and declared
    # post: returns true if rows are == to 50, this indicates there are more pages to load.
    #       returns false if rows are less than 50. indicates that there are no more pages to load and program should end.
    def __tableRowTraverse(self,soup):
        count = 0
        try:
            for tag in soup.table.tbody.find_all(re.compile("tr")):
             # counter increments in order to keep track of number of rows
                count += 1
                self.__tableColumnTraverse(tag)
            #print(self.__charts[-1].getChartName())
        except Exception:
            print("Invalid airport Id no charts found for " + self.__ident)
            return False
        if (count < 50):
            return False
        else:
            return True

    # pre:function takes no arguments
    # post:outputs string - current chart cycle for faa digital products query
    @staticmethod
    def getCurrentCycl():
        present = datetime.datetime.now()            # present time
        cycleBase = datetime.datetime(2016, 8, 18)   # reference point for faa cycles
        timeDelta = datetime.timedelta(days=28)      # used to increase date by 28 days. FAA chart cycle

        while ((cycleBase + timeDelta) <= present):  #loop while cycle date is less than current date.
            cycleBase = cycleBase + timeDelta

        cycleBase = cycleBase + timeDelta   # adds timeDelta one more time since faa cycle attribute is based on end of cycle
        cycleMonth = str(cycleBase.month)

        if (len(cycleMonth) == 1):          # if single digit month adds 0 to resulting string
            cycleMonth = "0" + cycleMonth

        return "?cycle=" + str(cycleBase.year)[2:] + cycleMonth



    #pre: function takes no arguments. private member __charts must be not empty.
    #post: returns array of Chart objects.
    def getCharts(self):
        if not self.__charts:
            raise Exception ("charts array is empty. must call scrape method with valid airportId param to load array")
        else:
            return self.__charts









