![](http://i.imgur.com/hgUWSf0.png)

# About

Wrapper for the Stock Data API.

# Getting Started

To get started, just add your API_TOKEN to the `settings.py file`

# Examples

Here are some examples for the API call.



## Print a sorted set of all tickers
`get_tickers()` - Returns a sorted set of all tickers

```
def main():
    for ticker in API.get_tickers():
        print(ticker)
```

results:
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


