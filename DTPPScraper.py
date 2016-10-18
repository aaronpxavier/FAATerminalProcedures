#!/usr/bin/env

from __future__ import print_function
import urllib.request
import re
import datetime
from chart import Chart
from bs4 import BeautifulSoup

class DTPPScraper:
    # pre: ident must be declared and defined with valid 3 or 4 character airport id.
    # post: stores scraped charts in charts[] private member and creates new instance of DTPPScraper class
    def __init__(self, ident):
        self.__ident = ident
        self.__charts = []
        page_count = 0
        IDENT_GET_PARAM =  "&ident=" + ident
        BASE_URL = "http://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/"
        CYCLE = self.get_current_cycl()
        url = BASE_URL + CYCLE + IDENT_GET_PARAM

        # loops through html pages in FAA chart results. finishes when all pages have been scraped
        while (True):
            # gets html document from FAA chart results
            B_SOUP = BeautifulSoup(urllib.request.urlopen(url),"html.parser")

            # increment is used in http get request attribute to cycle thru pages
            page_count += 1
            print ("Accessing charts for: " + ident)
            print("scraping page " + url)
            # loads next page if tableRowtravers() returns true, breaks loop if tableRowtravers() returns false
            if (self.__table_row_traverse(B_SOUP)):
                # creates new url for next page if there are more pages in result
                url = BASE_URL + CYCLE + IDENT_GET_PARAM + "&page=" + str(page_count+1)
            else:
                break

    #pre:method takes no argument. __charts[] private member must not be empty.
    #post:downloads pdf file for all Chart objects in private member __charts[].
    def download_charts(self):
        for chart in self.__charts:
            print("downloading " + chart.get_chart_name() +
              " from " + chart.get_pdf_url())
            try:
                REQUEST = urllib.request.urlopen(chart.get_pdf_url())
                chart.set_chart_data(REQUEST.read())
            except Exception:
                print("Could not download chart " + chart.get_chart_name())



    # traverses columns in page table
    # pre: tag must be declared and defined
    # post: traverses page table column. Creates Chart() object and appends Chart() obj to private member __charts[]
    def __table_col_traverse(self, tag):
        self.__charts.append(Chart())
        for index, tag in enumerate(tag.find_all(re.compile("td"))):
            #index values tracks the current column being scraped
            if index == 3 :
                airport_id = tag.text
                if airport_id[airport_id.find("(")+1:airport_id.find(")")] != "" :
                    self.__charts[-1].set_airport_id(airport_id[airport_id.find("(") + 1:airport_id.find(")")])
                else:
                    self.__charts[-1].set_airport_id(airport_id[:3])
            elif index == 4 :
                self.__charts[-1].set_region_name(tag.text)
            elif index == 6 :
                self.__charts[-1].set_procedure_name(tag.text)
            elif index == 7 :
                if tag.a:
                    chart_name = tag.text[:-6]+".pdf"
                    self.__charts[-1].set_pdf_url(tag.a['href'])
                    self.__charts[-1].set_chart_name(chart_name.replace("/", "_"))
        if self.__charts[-1].get_pdf_url() == '':
            self.__charts.pop()


    # traverses all rows in page table.
    # pre: soup is defined and declared
    # post: returns true if rows are == to 50, this indicates there are more pages to load.
    #       returns false if rows are less than 50 or if airport id is invlalid.
    #       indicates that there are no more pages to load and scraping should end.
    def __table_row_traverse(self, soup):
        count = 0
        try:
            for tag in soup.table.tbody.find_all(re.compile("tr")):
                count += 1   # counter increments in order to keep track of number of rows
                self.__table_col_traverse(tag)
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
    def get_current_cycl():
        PRESENT = datetime.datetime.now()            # present time
        TIME_DELTA = datetime.timedelta(days=28)  # used to increase date by 28 days. FAA chart cycle
        cycle_base = datetime.datetime(2016, 8, 18)   # reference point for faa cycles


        while ((cycle_base + TIME_DELTA) <= PRESENT):  #loop while cycle date is less than current date.
            cycle_base = cycle_base + TIME_DELTA

        cycle_base = cycle_base + TIME_DELTA   # adds TIME_DELTA one more time since faa cycle attribute is based on end of cycle
        cycle_month = str(cycle_base.month)

        if (len(cycle_month) == 1):          # if single digit month adds 0 to resulting string
            cycle_month = "0" + cycle_month

        return "?cycle=" + str(cycle_base.year)[2:] + cycle_month



    #pre: function takes no arguments. private member __charts must be not empty.
    #post: returns array of Chart objects.
    def get_charts(self):
        if not self.__charts:
            raise Exception ("charts array is empty.")
        else:
            return self.__charts









