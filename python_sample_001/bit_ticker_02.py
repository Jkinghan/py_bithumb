import pybithumb
import time

btc = pybithumb.get_current_price("BTC")
btc2 = pybithumb.get_ohlcv("BTC")
close = btc2['close']

window = close.rolling(5)
ms5 = window.mean()
print(ms5)
