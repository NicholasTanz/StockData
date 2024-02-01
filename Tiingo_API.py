'''
Tinngo_API.py  

This file contains basic examples of how to use the Tiingo API to get stock data.
(Might remove this file in the future)
'''

import requests
import json

# Documentation: https://api.tiingo.com/documentation/general/overview
TIINGO_API_KEY = '' # Your API Key from Tiingo. (https://blog.tiingo.com/how-to-find-your-tiingo-api-token/)
def test_connection():
    ''' Test the connection to the Tiingo API. '''
    headers = {
        'Content-Type': 'application/json',
        'Authorization' : f'Token {TIINGO_API_KEY}'
        }
    requestResponse = requests.get("https://api.tiingo.com/api/test/",
                                    headers=headers)
    
    print(requestResponse.json())
    return requestResponse.status_code == 200                    



def TiingoRequestDailyData(ticker):
    ''' Make a request to the Tiingo API to get daily data for the specified stock. '''

    url = f'https://api.tiingo.com/tiingo/daily/{ticker}'

    # Set up the request headers with the API key
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {TIINGO_API_KEY}'
    }

    # Make the API request
    response = requests.get(url, headers=headers)

    if response.status_code == 200: # successful request
        data = response.json()
        return data

    else:
        # Print an error message if the request was not successful
        print(f'Error: {response.status_code} - {response.text}')
        return None

def test_TiingoRequestDailyData(tickers: list):
    ''' Test the TiingoRequestDailyData function. '''
    for ticker in tickers:
        data = TiingoRequestDailyData(ticker)
        if data is None:
            return False
        else:
            print(f'{ticker} data: {json.dumps(data, indent=2)}')

    return True


if(__name__ == "__main__"):
    assert(test_connection())
    assert(test_TiingoRequestDailyData(tickers=['AAPL']))