'''
Created on May 31, 2015

@author: Horia
'''
import datetime
import numpy as np
import pandas as pd
import pandas.io.data as web
import urllib2

def getTenYearNoteYield(start, end):
    #start = datetime.datetime(2000, 1, 1)
    #end = datetime.datetime(2013, 1, 1)
    pdf = web.DataReader('^TNX', 'yahoo', start, end)
    return pdf['Close'].mean()

if __name__ == '__main__':
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime(2013, 1, 1)
    #print pdf['Close'].mean()