import json
import requests

"""
Connects to Stock Data API
"""


class StockDataApi:

    def __init__(self, ip_address, port, api_token):
        self.ip_address = ip_address
        self.port = port
        self.api_token = api_token

    # Returns a sorted set of all tickers
    def get_tickers(self):
        tickers = set()
        r = requests.get(self.get_api_url('companies'))
        if r.status_code != 200:
            print('Could not get tickers')
            return False
        for company in json.loads(r.text):
            tickers.add(company['ticker'])
        return sorted(tickers)

    # Returns a list of all companies
    def get_companies(self):
        r = requests.get(self.get_api_url('companies'))
        if r.status_code != 200:
            print('Could not get companies')
            return False
        return json.loads(r.text)

    # Returns single company as dict
    def get_single_company(self, ticker):
        r = requests.get(self.get_api_url('companies') + '/' + ticker + '/')
        if r.status_code != 200:
            print('Could not get ' + ticker)
            return False
        return json.loads(r.text)

    # Returns a list of historical price dicts (date, open, high, low, etc...)
    def get_history(self, ticker):
        r = requests.get(self.get_api_url('history') + '/' + ticker + '/')
        if r.status_code != 200:
            print('Could not get history for ' + ticker)
            return False
        return json.loads(r.text)

    # Returns historical price dict for a single date
    def get_history_for_date(self, ticker, date):
        r = requests.get(self.get_api_url('history') + '/' + ticker + '/' + date + '/')
        if r.status_code != 200:
            print('Could not get history for ' + ticker + ' on ' + date)
            return False
        return json.loads(r.text)

    # Returns a list of historical price dicts between date range
    def get_history_for_date_range(self, ticker, start, end):
        r = requests.get(self.get_api_url('history') + '/' + ticker + '/' + start + '/' + end + '/')
        if r.status_code != 200:
            print('Could not get history for ' + ticker + ' for that date range')
            return False
        return json.loads(r.text)

    def get_api_url(self, keyword):
        url = 'http://' + self.ip_address
        if self.port is not '':
            url += ':' + self.port
        url += '/v1/' + self.api_token + '/' + keyword + '/'
        return url
