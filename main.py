from settings import *
from v1.stock_data_api import StockDataApi


API = StockDataApi(IP_ADDRESS, PORT, API_TOKEN)


def main():
    for row in API.get_history_for_date_range('GOOG', '2012-07-16', '2012-07-18'):
        print(row)


if __name__ == "__main__":
    main()
