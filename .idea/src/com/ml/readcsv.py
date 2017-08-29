import pandas as pd

class readdata:

    def readcsv(self):
        nasdaqdata = pd.read_csv('nasdaq.csv')
        print nasdaqdata.head(5)
        print nasdaqdata.describe()
        print nasdaqdata.info()
        print '\n'
        print nasdaqdata.isnull().sum()



obj_nasdaqdata = readdata()
obj_nasdaqdata.readcsv()
