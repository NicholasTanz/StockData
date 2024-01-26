import requests
from datetime import datetime, timedelta

# API Key from Tiingo (https://api.tiingo.com/)
TIINGO_API_KEY = ''

def get_current_date():
    ''' Returns the current date in the format YYYY-MM-DD. '''
    return datetime.today().strftime('%Y-%m-%d')

def get_past_date(days):
    ''' Returns the date from the specified number of days ago in the format YYYY-MM-DD. '''
    return (datetime.today() - timedelta(days=days)).strftime('%Y-%m-%d')