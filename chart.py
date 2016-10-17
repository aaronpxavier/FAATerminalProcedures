#!/usr/bin/env


class Chart:

    def __init__ (self):
        self.__airport_id = ''
        self.__region_name = ''
        self.__procedure_name = ''
        self.__pdf_url = ''
        self.__chart_name = ''
        self.__chart_pdf_file = None

    # pre: string airport_id must be declared and defined as a valid 3 or 4 character airport id.
    # post: stores airport_id in private member __airport_id
    def setAirportID(self, airport_id):
        self.__airport_id = airport_id

    # pre: string region_name must be declared and defined.
    # post: stores region_name in private member __region_name
    def setRegionName(self, region_name):
        self.__region_name = region_name

    # pre: string procedure_name must be declared and defined.
    # post: stores procedure_name in private member __procedure_name
    def setProcedureName(self, procedure_name):
        self.__procedure_name = procedure_name

    # pre: string pdf_url must be declared and defined with valid url string.
    # post: stores pdf_url in private member __pdf_url
    def setPDFURL(self, pdf_url):
        self.__pdf_url = pdf_url

    # pre: string chart_name must be declared and defined.
    # post: stores chart_name in private member __chart_name
    def setChartName(self, chart_name):
        self.__chart_name = chart_name

    # pre: data_in must be declared and defined with PDF file
    # post: pdf file is stored in private member __chart_pdf_file
    def setChartData(self, data_in):
        self.__chart_pdf_file = data_in

    # pre: method takes no arguments
    # post: returns private member of type string __airport_id
    def getAirportID(self):
        return self.__airport_id

    # pre: method takes no arguments
    # post: returns private member of type string __region_name
    def getRegionName(self):
        return self.__region_name

    # pre: method takes no arguments
    # post: returns string private member of type string __procedure_name
    def getProcedureName(self):
        return self.__procedure_name

    # pre: method takes no arguments
    # post: returns private member of type string __pdf_url
    def getPDFURL(self):
        return self.__pdf_url

    # pre: method takes no arguments
    # post: returns private member of type string __chart_name
    def getChartName(self):
        return self.__chart_name

    # pre: method takes no arguments. private member __chart_pdf_file must be loaded with pdf data.
    # post: returns private member of type pdf file data chartPDFFile
    def getChartData(self):
        if self.__chart_pdf_file == '':
            raise Exception("no chart data in Chart obj " + self.__chart_name)
        else:
            return self.__chart_pdf_file



