# RSI Calculator
A library to calculating RSI.
# Install
```
pip3 install rsi-calculator
```
# Using
## In another script
```python
from rsi_calculator import rsi
# rsi(prices = None, periods = 14)
print(rsi([15, 20, 25, 30, 20, 15, 20, 25, 30, 20, 15, 20, 25, 30, 100]))
```
## In command line
```console
  -h, --help            show this help message and exit
  -pr PRICES [PRICES ...], --prices PRICES [PRICES ...]
                        Prices
  -pe PERIODS, --periods PERIODS
                        Periods
```
```console
rsi -pr 15 20 25 30 20 15 20 25 30 20 15 20 25 30 100
```