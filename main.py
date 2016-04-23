from settings import *
from v1.stock_data_api import StockDataApi


API = StockDataApi(IP_ADDRESS, PORT, API_TOKEN)


def main():
    for company in API.get_companies():
        print(company)


if __name__ == "__main__":
    main()
