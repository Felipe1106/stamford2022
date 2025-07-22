from boto3 import resource
from dataclasses import dataclass
from decimal import Decimal
from dotenv import load_dotenv
from os import getenv
from s3_helper import CSVStream
from typing import Any

load_dotenv()

BUY = "buy"
SELL = "sell"

BUCKET = getenv("BUCKET_NAME")

XBT_2018_KEY = "xbt.usd.2018"
XBT_2020_KEY = "xbt.usd.2020"

ETH_2018_KEY = "eth.usd.2018"
ETH_2020_KEY = "eth.usd.2020"

S3 = resource("s3")
SELECT_ALL_QUERY = 'SELECT * FROM S3Object'
STREAM = CSVStream(
     'select',
     S3.meta.client,
     key=XBT_2018_KEY,
     bucket=BUCKET,
     expression=SELECT_ALL_QUERY,)
def algorithm(csv_row: str, context: dict[str, Any],):
    wallet = 1000000
    bitcoin = 0
    data = csv_row.split(',')
    price = data[1]
    if len(prices) > 20:
        pricesnew = prices[(len(prices) // 2):]

        # if len(pricesnew) < 5:
        # return "NONE"

    if csv_row.find('xbt') != -1:
        prices.append(float(price))
        if pricesnew[0] < pricesnew[-1]:
            #if bitcoin == 0:
               ##else:
            wallet += float(price)
            bitcoin -= 1
            return "SELL"

        elif pricesnew[0] > pricesnew[-1]:
            bitcoin += 1
            wallet -= float(price)
            return "BUY", wallet
        else:
            return "NONE"

    if len(prices2) > 20:
        pricesnew2 = prices2[(len(prices) // 2):]
    if csv_row.find('eth') != -1:
        prices2.append(float(price))
        if pricesnew2[0] < pricesnew2[-1]:
            return "BUY"
        elif pricesnew2[0] > pricesnew2[-1]:
            return "SELL"
        else:
            return "NONE"

if __name__ == '__main__':
     prices2 = []
     prices = []
     length = len(prices)
     for row in STREAM.iter_records():
         try:
            print(algorithm(row,[]))
         except Exception:
            print("NONE")
            continue
