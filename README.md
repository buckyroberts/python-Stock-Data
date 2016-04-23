![](http://i.imgur.com/hgUWSf0.png)

# About

Wrapper for the Stock Data API.

## Getting Started

To get started, just add your API_TOKEN to the `settings.py file`

### Print a sorted set of all tickers
```
def main():
    for ticker in API.get_tickers():
        print(ticker)
```

Response:
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

##Print basic information such as ticker symbol, name, market cap, IPO year, sector, and industry for all companies.

Sample code:
```
def main():
    for company in API.get_companies():
        print(company)
```

Response:
```
{'ipo_year': '2014', 'name': 'Amec Plc Ord', 'sector': 'Consumer Services', 'last_sale': '7.25', 'industry': 'Military/Government/Technical', 'ticker': 'AMFW', 'market_cap': '$2.85B'}
{'ipo_year': 'n/a', 'name': 'Affiliated Managers Group, Inc.', 'sector': 'Finance', 'last_sale': '174.91', 'industry': 'Investment Managers', 'ticker': 'AMG', 'market_cap': '$9.45B'}
{'ipo_year': '1983', 'name': 'Amgen Inc.', 'sector': 'Health Care', 'last_sale': '164.35', 'industry': 'Biotechnology: Biological Products (No Diagnostic Substances)', 'ticker': 'AMGN', 'market_cap': '$123.61B'}
```

## Print a specific field for all companies

Sample code:
```
def main():
    for company in API.get_companies():
        print(company)
```

Response:
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