#!/usr/bin/env


class Chart:

    def __init__ (self):
        self.__airportID = ''
        self.__regionName = ''
        self.__procedureName = ''
        self.__PDFURL = ''
        self.__chartName = ''
        self.__chartPDFFile = None

    # pre: stringIn must be declared and defined as a valid 3 or 4 character airport id.
    # post: stores stringIn in private member airportID
    def setAirportID(self, stringIn):
        self.__airportID = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in private member regionName
    def setRegionName(self,stringIn):
        self.__regionName = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in private member procedureName
    def setProcedureName(self,stringIn):
        self.__procedureName = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in private member PDFURL
    def setPDFURL(self,stringIn):
        self.__PDFURL = stringIn

    # pre: stringIn must be declared and defined.
    # post: stores stringIn in private member chartName
    def setChartName(self,stringIn):
        self.__chartName = stringIn

    # pre: dataIn must be declared and defined with PDF file
    # post: pdf file is stored in private member chartPDFFile
    def setChartData(self, dataIn):
        self.__chartPDFFile = dataIn

    # pre: method takes no arguments
    # post: returns private member of type string airportID
    def getAirportID(self):
        return self.__airportID

    # pre: method takes no arguments
    # post: returns private member of type string airportID
    def getRegionName(self):
        return self.__regionName

    # pre: method takes no arguments
    # post: returns string private member of type string procedureName
    def getProcedureName(self):
        return self.__procedureName

    # pre: method takes no arguments
    # post: returns private member of type string PDFURL
    def getPDFURL(self):
        return self.__PDFURL

    # pre: method takes no arguments
    # post: returns private member of type string chartName
    def getChartName(self):
        return self.__chartName

    # pre: method takes no arguments. private member chartPDFFile must be not empty.
    # post: returns private member of type pdf file data chartPDFFile
    def getChartData(self):
        if self.__chartPDFFile == '':
            raise Exception("no chart data in Chart obj " + self.__chartName)
        else:
            return self.__chartPDFFile



