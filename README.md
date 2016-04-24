![](http://i.imgur.com/hgUWSf0.png)

# About

This is a wrapper for the [Stock Data API](http://stock-data-api.com/).

# Getting Started

To get started, just add your API_TOKEN to the `settings.py file`

# Examples

Here are a few examples for using the API and a brief description of the functions used.

## Print a sorted set of all tickers
`get_tickers()` - Returns a sorted set of all tickers

```
def main():
    for ticker in API.get_tickers():
        print(ticker)
```

output:
```
A
AA
AAAP
AAC
AAL
AAMC
AAME
...
```

## Print all companies
`get_companies()` - Returns a list of all companies

```
def main():
    for company in API.get_companies():
        print(company['name'] + ' - ' + company['market_cap'])
```

output:
```
Agilent Technologies, Inc. - $13.74B
Alcoa Inc. - $13.7B
Advanced Accelerator Applications S.A. - $1.37B
AAC Holdings, Inc. - $462.24M
American Airlines Group, Inc. - $24.13B
Altisource Asset Management Corp - $32.81M
Atlantic American Corporation - $92.59M
...
```

## View a single company
`get_single_company()` - Returns single company as dict

```
def main():
    print(API.get_single_company('FB'))
```

output:
```
{
   'ticker':'AMZN',
   'market_cap':'$297.1B',
   'industry':'Catalog/Specialty Distribution',
   'last_sale':'631',
   'sector':'Consumer Services',
   'ipo_year':'1997',
   'name':'Amazon.com, Inc.'
}
```

## Get historical price data
`get_history()` - Returns a list of historical price dicts (date, open, high, low, etc...)

```
def main():
    for row in API.get_history('GOOG'):
        print(row)
```

output:
```
{'change_24h': 21.6, 'adj_close': 317.16, 'sma_10': 601.57, 'low': 617.5, 'ticker': 'GOOG', 'open': 618.89, 'obv': -1365688700.0, 'sma_5': 615.88, 'pct_change': 2.6, 'sma_200': 605.05, 'change': 16.07, 'sma_50': 584.83, 'sto': 99.95, 'high': 635.0, 'rsi_14': 71.9, 'date': '2012-07-27', 'close': 634.96, 'pct_change_24h': 3.52, 'volume': 7125900, 'rsi_10': 77.59}
{'change_24h': -2.66, 'adj_close': 315.83, 'sma_10': 607.31, 'low': 629.5, 'ticker': 'GOOG', 'open': 636.05, 'obv': -1361299000.0, 'sma_5': 619.24, 'pct_change': -0.59, 'sma_200': 605.47, 'change': -3.75, 'sma_50': 585.01, 'sto': 87.21, 'high': 642.6, 'rsi_14': 69.97, 'date': '2012-07-30', 'close': 632.3, 'pct_change_24h': -0.42, 'volume': 4389700, 'rsi_10': 74.74}
{'change_24h': 0.67, 'adj_close': 316.17, 'sma_10': 612.93, 'low': 628.22, 'ticker': 'GOOG', 'open': 628.26, 'obv': -1365044100.0, 'sma_5': 624.32, 'pct_change': 0.75, 'sma_200': 605.84, 'change': 4.71, 'sma_50': 585.66, 'sto': 88.04, 'high': 636.5, 'rsi_14': 70.19, 'date': '2012-07-31', 'close': 632.97, 'pct_change_24h': 0.11, 'volume': 3745100, 'rsi_10': 75.0}
```

## Get historical price data (single date)
`get_history_for_date()` - Returns historical price dict for a single date

```
def main():
    print(API.get_history_for_date('GOOG', '2012-07-16'))
```

output:
```
{
   'high':579.19,
   'open':576.37,
   'rsi_10':47.59,
   'adj_close':287.17,
   'sma_50':585.8,
   'rsi_14':47.54,
   'sto':41.33,
   'pct_change_24h':-0.28,
   'pct_change':-0.25,
   'sma_5':574.96,
   'obv':-1345097800.0,
   'change_24h':-1.6,
   'volume':2936100,
   'sma_10':581.1,
   'change':-1.45,
   'close':574.92,
   'date':'2012-07-16',
   'ticker':'GOOG',
   'low':571.78,
   'sma_200':601.12
}
```

## Get historical price data (date range)
`get_history_for_date_range()` - Returns a list of historical price dicts between date range

```
def main():
    for row in API.get_history_for_date_range('GOOG', '2012-07-16', '2012-07-18'):
        print(row)
```

output:
```
{'sma_50': 585.8, 'date': '2012-07-16', 'ticker': 'GOOG', 'sma_5': 574.96, 'change': -1.45, 'close': 574.92, 'sma_200': 601.12, 'rsi_10': 47.59, 'adj_close': 287.17, 'low': 571.78, 'pct_change_24h': -0.28, 'rsi_14': 47.54, 'sto': 41.33, 'pct_change': -0.25, 'change_24h': -1.6, 'volume': 2936100, 'sma_10': 581.1, 'high': 579.19, 'obv': -1345097800.0, 'open': 576.37}
{'sma_50': 585.39, 'date': '2012-07-17', 'ticker': 'GOOG', 'sma_5': 573.97, 'change': -1.7, 'close': 576.73, 'sma_200': 601.36, 'rsi_10': 49.38, 'adj_close': 288.08, 'low': 568.4, 'pct_change_24h': 0.31, 'rsi_14': 48.72, 'sto': 45.55, 'pct_change': -0.29, 'change_24h': 1.81, 'volume': 3372700, 'sma_10': 580.73, 'high': 580.67, 'obv': -1348470500.0, 'open': 578.43}
{'sma_50': 584.86, 'date': '2012-07-18', 'ticker': 'GOOG', 'sma_5': 575.88, 'change': 3.78, 'close': 580.76, 'sma_200': 601.69, 'rsi_10': 53.32, 'adj_close': 290.09, 'low': 576.13, 'pct_change_24h': 0.7, 'rsi_14': 51.34, 'sto': 54.96, 'pct_change': 0.66, 'change_24h': 4.03, 'volume': 3107900, 'sma_10': 580.02, 'high': 583.69, 'obv': -1351578400.0, 'open': 576.98}
```

# Links

* [Stock Data API](http://stock-data-api.com/)
* [Twitter](https://twitter.com/StockMarketAPI)
* [Facebook](https://www.facebook.com/Stock-Data-API-613005355529673/)
* [Pinterest](https://www.pinterest.com/stockdataapi/)
* [reddit](https://www.reddit.com/r/stock_data/)
* [Tumblr](http://stockdataapi.tumblr.com/)
