"""
Finance data preprocessing
"""
""
#for test
import pandas as pd
import os, sys
#import xlrd

class DataManager:

    def getCSVData(self,name="hsi_futures_jan"):
        self.df = pd.read_csv("E:\\hsi_futures_jan.csv")
        self.df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d/%m/%Y %H:%M')
        self.df.sort_values("Date", ascending=True, inplace=True)
        data = self.df.set_index([range(self.df.shape[0])])
        return data

    def getExcelData(self):
        pass

    def getExcelSheetData(self, excel, sheet):
        """
        get data from 'hsi_futures.xlsx'
        Date | Open | High | Low | Close | SMAVG5 | SMAVG10 | SMAVG15 | Volume | VolumeSMAVG5
        :return: data table
        """
        self.df = pd.DataFrame()
        #xl = pd.ExcelFile("../Data/hsi_futures.xlsx")
        # print xl.sheet_names
        #sheets = xl.sheet_names
        #for sheet in sheets:
        self.df = self.df.append(pd.read_excel(excel, sheet))
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.sort_values("Date", ascending=True, inplace=True)
        data = self.df.set_index([range(self.df.shape[0])])
        return data

    def getInterval(self, start, end):
        """
        Includes both start and end
        :param start    : start date (e.g start = '2016-01-26 14:45:00')
        :param end      : end date (e.g end = '2016-02-26 14:45:00')
        :return         : data between start and end
        """
        interval = (self.df['Date'] >= start) & (self.df['Date'] <= end)
        _df = self.df.loc[interval]
        data = _df.set_index([range(_df.shape[0])])
        return data

    @staticmethod
    def toFloatArray(df):
        dt_array = list(df.values)
        float_array = map(float, dt_array)
        return float_array

    #d = getExcelData()
    #print inte
'''
#test data input and getInterval
dm = DataManager()
d = dm.getExcelData()
inte = dm.getInterval('2016-01-26 14:45:00', '2016-02-26 16:00:00')
print inte
'''