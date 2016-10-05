#!/usr/bin/env python

from __future__ import print_function
import urllib.request
import re
import datetime
from chart import Chart
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self):
        self.__charts = []


    # traverses columns in page table
    # pre: tag must be declared and defined
    # post: traverses page table column. returns chart object.
    def __tableColumnTraverse(self,tag):
        tdCounter = 0
        self.__charts.append(Chart())
        for tag in tag.find_all(re.compile("td")):
            if tdCounter == 3 :
                airportID = tag.text
                if airportID[airportID.find("(")+1:airportID.find(")")] != "" :
                    self.__charts[-1].setAirportID(airportID[airportID.find("(") + 1:airportID.find(")")])
                else:
                    self.__charts[-1].setAirportID(airportID[:3])
            if tdCounter == 4 :
                self.__charts[-1].setRegionName(tag.text)
            elif tdCounter == 6 :
                self.__charts[-1].setProcedureName(tag.text)
            elif tdCounter == 7 :
                if tag.a:
                    chartName = tag.text[:-6]+".pdf"
                    self.__charts[-1].setPDFURL(tag.a['href'])
                    self.__charts[-1].setChartName(chartName.replace("/", "_"))
            tdCounter += 1

    # traverses all rows in page table.
    # pre: soup and cnx are defined and declared
    # post: returns true if rows are == to 50, this indicates there are more pages to load.
    #       returns false if rows are less than 50. indicates that there are no more pages to load and program should end.
    def __tableRowTraverse(self,soup):
        count = 0
        for tag in soup.table.tbody.find_all(re.compile("tr")):
            # counter increments in order to keep track of number of rows
            count+=1
            self.__tableColumnTraverse(tag)
            print(self.__charts[-1].getChartName())
        if (count < 50):
            return False
        else:
            return True

    # pre:function takes no arguments
    # post:outputs string - current chart cycle for faa digital products query
    def getCurrentCycl(self):
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

    #pre: identIn must be declared and defined with valid 3 or 4 character airport id.
    #post: stores charts in charts[] attribute.
    def parse(self,identIn):
        pageCount = 0
        ident = "&ident=" + identIn
        baseurl = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/"
        cycle = self.getCurrentCycl()

        url = baseurl + cycle + ident
        # loops through html pages in FAA chart results. finishes when all pages have been scraped
        while (True):
            # gets html document from FAA chart results
            bSoup = BeautifulSoup(urllib.request.urlopen(url),"html.parser")
            print (url)
            # increment is used in http get request attribute to cycle thru pages
            pageCount += 1
            print ("Page #: " + str(pageCount))

            # loads next page if tableRowtravers() returns true, breaks loop if tableRowtravers() returns false
            if (self.__tableRowTraverse(bSoup)):
                # creates new url for next page if there are more pages in result
                url = baseurl + cycle + ident + "&page=" + str(pageCount+1)
            else:
                break

    #pre: function takes no arguments.
    #post: returns array of Chart objects.
    def getCharts(self):
        return self.__charts



