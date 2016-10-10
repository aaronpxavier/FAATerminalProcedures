#!/usr/bin/env


class Chart:

    def __init__ (self):
        self.__airportID = ''
        self.__regionName = ''
        self.__procedureName = ''
        self.__PDFURL = ''
        self.__chartName = ''
        self.__chartPDFFile = None

    #pre: stringIn must be declared and defined as a valid 3 or 4 character airport id.
    #post: stores stringIn in airportID attribute.
    def setAirportID(self, stringIn):
        self.__airportID = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in regionName attribute.
    def setRegionName(self,stringIn):
        self.__regionName = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in procedureName attribute.
    def setProcedureName(self,stringIn):
        self.__procedureName = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in PDFURL attribute.
    def setPDFURL(self,stringIn):
        self.__PDFURL = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in chartName attribute.
    def setChartName(self,stringIn):
        self.__chartName = stringIn

    # pre: dataIn
    def setChartData(self, dataIn):
        self.__chartPDFFile = dataIn

    # pre: method takes no arguments
    # post: returns string airportID
    def getAirportID(self):
        return self.__airportID

    # pre: method takes no arguments
    # post: returns string airportID
    def getRegionName(self):
        return self.__regionName

    # pre: method takes no arguments
    # post: returns string procedureName
    def getProcedureName(self):
        return self.__procedureName

    # pre: method takes no arguments
    # post: returns string PDFURL
    def getPDFURL(self):
        return self.__PDFURL

    # pre: method takes no arguments
    # post: returns string chartName
    def getChartName(self):
        return self.__chartName

    # pre: method takes no arguments
    # post: returns pdf file data from chartPDFFile attribute
    def getChartData(self):
        if self.__chartPDFFile == ' ':
            print("no chart data in Chart Object")
        return self.__chartPDFFile



