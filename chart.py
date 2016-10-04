
import urllib.request




class Chart:
    def __init__ (self):
        self.__airportID = ' '
        self.__regionName = ' '
        self.__procedureName = ' '
        self.__PDFURL = ' '
        self.__chartName = ' '
        self.__chartData  = ' '

    def setAirportID(self, stringIn):
        self.__airportID = stringIn

    def setRegionName(self,stringIn):
        self.__regionName = stringIn

    def setProcedureName(self,stringIn):
        self.__procedureName = stringIn

    def setPDFURL(self,stringIn):
        self.__PDFURL = stringIn

    def setChartName(self,stringIn):
        self.__chartName = stringIn

    def getAirportID(self):
        return self.__airportID

    def getRegionName(self):
        return self.__regionName

    def getProcedureName(self):
        return self.__procedureName

    def getPDFURL(self):
        return self.__PDFURL

    def getChartName(self):
        return self.__chartName

    def downLoadChart(self):
        with urllib.request.urlopen(self.__PDFURL) as chartData:
            print("downloading " + self.__chartName + " from " + self.__PDFURL)
            self.__chartData = chartData
    def getChartData(self):
        if self.__chartData == ' ':
            print("no chart data in Chart Object")
        return self.__chartData
    



