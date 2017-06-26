# Create your models here.
import datetime
import urllib2

from django.db import models

import numpy as np
import pandas as pd
import pandas.io.data as web
from helperclasses import sharpe_helper


class Sharpe(models.Model):
    ticker = models.CharField(max_length=4, help_text = 'Market Symbol')
    trade_period = models.IntegerField(default=252)
    startDate = models.DateField('Start Date')
    endDate = models.DateField('End Date')
    tenYearNoteYield = models.FloatField(default=5.0)
    benchmarkList = ( 
                     ('SPY', 'SPDR S&P 500 ETF (SPY)' ),
                     ('VOO','Vanguard S&P 500 ETF (VOO)'),
                     ('IVV' ,'iShares Core S&P 500 (IVV)'),
                     )
    benchmark = models.CharField( default= 'SPY', max_length=4, choices = benchmarkList )
    
    def risk_free_rate(self):
        #('^TNX', 'yahoo', self.startDate, self.endDate)
        self.tenYearNoteYield = sharpe_helper.getTenYearNoteYield(self.startDate, self.endDate)
        
        return self.tenYearNoteYield
    
    def equity_sharpe(self):
        """
        Calculates the annualized Sharpe ratio based on the daily
        returns of an equity ticker symbol listed in Google Finance.
    
        """
    
        # Obtain the equities daily historic data for the desired time trade_period
        # and add to a pandas DataFrame
        pdf = web.DataReader(self.ticker, 'google', self.startDate, self.endDate)
    
        # Use the percentage change method to easily calculate daily returns
        pdf['daily_ret'] = pdf['Close'].pct_change()
    
        riskFreeRate = self.tenYearNoteYield / 100
        pdf['excess_daily_ret'] = pdf['daily_ret'] - riskFreeRate / 252
        
        returns = pdf['excess_daily_ret']
        
        return np.sqrt(self.trade_period) * returns.mean() / returns.std()
    
    def market_neutral_sharpe(self):
        """
        Calculates the annualised Sharpe ratio of a market
        neutral long/short strategy involving the long of 'ticker'
        with a corresponding short of the 'benchmark'.
        """
    
        # Get historic data for both a symbol/ticker and a benchmark ticker
        tick = web.DataReader(self.ticker, 'google', self.startDate, self.endDate)
        bench = web.DataReader(self.benchmark, 'google', self.startDate, self.endDate)
    
        # Calculate the percentage returns on each of the time series
        tick['daily_ret'] = tick['Close'].pct_change()
        bench['daily_ret'] = bench['Close'].pct_change()
    
        # Create a new DataFrame to store the strategy information
        # The net returns are (long - short)/2, since there is twice
        # the trading capital for this strategy
        strat = pd.DataFrame(index=tick.index)
        strat['net_ret'] = (tick['daily_ret'] - bench['daily_ret'])/2.0
        
        returns = strat['net_ret']
        
        # Return the annualised Sharpe ratio for this strategy
        return np.sqrt(self.trade_period) * returns.mean() / returns.std()
    
    risk_free_rate.short_description = '10 Year US Bond Yield Period Average %'    