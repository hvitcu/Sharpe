from django.contrib import admin
from sharpeapp.models import Sharpe

# Register your models here.

class SharpeAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'trade_period', 'startDate', 'endDate', 'risk_free_rate', 'equity_sharpe', 'market_neutral_sharpe', 'benchmark']
    
admin.site.register(Sharpe, SharpeAdmin)
    