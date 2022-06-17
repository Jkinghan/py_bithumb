import pybithumb
import time
import datetime

tickers = pybithumb.get_tickers()
detail = pybithumb.get_market_detail("BTC")
#print(detail)
orderbook = pybithumb.get_orderbook("BTC")
#print(orderbook)

#for k in orderbook:
#    print(k)

ms = int(orderbook["timestamp"])
dt = datetime.datetime.fromtimestamp(ms/1000)
print(dt)
bids = orderbook['bids'] # 매도 호가
asks = orderbook['asks'] # 매수 호가
print(bids, asks)

#print(orderbook['payment_currency'])
#print(orderbook['order_currency'])

#for ticker in tickers:
#    price = pybithumb.get_current_price(ticker)
#    print(ticker, price)
#    time.sleep(0.1)