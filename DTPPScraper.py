#!/usr/bin/env

from __future__ import print_function
import urllib.request
import re
import datetime
from chart import Chart
from bs4 import BeautifulSoup

class DTPPScraper:
    # pre: identIn must be declared and defined with valid 3 or 4 character airport id.
    # post: stores scraped charts in charts[] private member and creates new instance of DTPPScraper class
    def __init__(self, identIn):
        self.__ident = identIn
        self.__charts = []
        page_count = 0
        IDENT_GET_PARAM =  "&ident=" + identIn
        BASE_URL = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/"
        CYCLE = self.getCurrentCycl()
        url = BASE_URL + CYCLE + IDENT_GET_PARAM

        # loops through html pages in FAA chart results. finishes when all pages have been scraped
        while (True):
            # gets html document from FAA chart results
            bSoup = BeautifulSoup(urllib.request.urlopen(url),"html.parser")

            # increment is used in http get request attribute to cycle thru pages
            page_count += 1
            print ("Accessing charts for: " + identIn)
            print("scraping page " + url)
            # loads next page if tableRowtravers() returns true, breaks loop if tableRowtravers() returns false
            if (self.__tableRowTraverse(bSoup)):
                # creates new url for next page if there are more pages in result
                url = BASE_URL + CYCLE + IDENT_GET_PARAM + "&page=" + str(page_count+1)
            else:
                break

    #pre:method takes no argument. __charts[] private member must not be empty.
    #post:downloads pdf file for all Chart objects in private member __charts[].
    def downloadCharts(self):
        for chart in self.__charts:
            print("downloading " + chart.getChartName() +
              " from " + chart.getPDFURL())
            try:
                REQUEST = urllib.request.urlopen(chart.getPDFURL())
                chart.setChartData(REQUEST.read())
            except Exception:
                print("Could not download chart " + chart.getChartName())



    # traverses columns in page table
    # pre: tag must be declared and defined
    # post: traverses page table column. Creates Chart() object and appends Chart() obj to private member __charts[]
    def __tableColumnTraverse(self,tag):
        self.__charts.append(Chart())
        for index, tag in enumerate(tag.find_all(re.compile("td"))):
            #index values tracks the current column being scraped
            if index == 3 :
                airport_id = tag.text
                if airport_id[airport_id.find("(")+1:airport_id.find(")")] != "" :
                    self.__charts[-1].setAirportID(airport_id[airport_id.find("(") + 1:airport_id.find(")")])
                else:
                    self.__charts[-1].setAirportID(airport_id[:3])
            elif index == 4 :
                self.__charts[-1].setRegionName(tag.text)
            elif index == 6 :
                self.__charts[-1].setProcedureName(tag.text)
            elif index == 7 :
                if tag.a:
                    chart_name = tag.text[:-6]+".pdf"
                    self.__charts[-1].setPDFURL(tag.a['href'])
                    self.__charts[-1].setChartName(chart_name.replace("/", "_"))
        if self.__charts[-1].getPDFURL() == '':
            self.__charts.pop()


    # traverses all rows in page table.
    # pre: soup is defined and declared
    # post: returns true if rows are == to 50, this indicates there are more pages to load.
    #       returns false if rows are less than 50 or if airport id is invlalid.
    #       indicates that there are no more pages to load and scraping should end.
    def __tableRowTraverse(self,soup):
        count = 0
        try:
            for tag in soup.table.tbody.find_all(re.compile("tr")):
                count += 1   # counter increments in order to keep track of number of rows
                self.__tableColumnTraverse(tag)
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
        PRESENT = datetime.datetime.now()            # present time
        CYCLE_BASE = datetime.datetime(2016, 8, 18)   # reference point for faa cycles
        TIME_DELTA = datetime.timedelta(days=28)      # used to increase date by 28 days. FAA chart cycle

        while ((CYCLE_BASE + TIME_DELTA) <= PRESENT):  #loop while cycle date is less than current date.
            CYCLE_BASE = CYCLE_BASE + TIME_DELTA

        CYCLE_BASE = CYCLE_BASE + TIME_DELTA   # adds TIME_DELTA one more time since faa cycle attribute is based on end of cycle
        cycle_month = str(CYCLE_BASE.month)

        if (len(cycle_month) == 1):          # if single digit month adds 0 to resulting string
            cycle_month = "0" + cycle_month

        return "?cycle=" + str(CYCLE_BASE.year)[2:] + cycle_month



    #pre: function takes no arguments. private member __charts must be not empty.
    #post: returns array of Chart objects.
    def getCharts(self):
        if not self.__charts:
            raise Exception ("charts array is empty.")
        else:
            return self.__charts









