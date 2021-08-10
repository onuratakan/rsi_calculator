import numpy as np
import argparse


def rsi(prices = None, periods = 14):
    parser = argparse.ArgumentParser()
    parser.add_argument('-pr', '--prices', nargs="+", type=float, help='Prices')
    parser.add_argument('-pe', '--periods', type=int, help='Periods')

    args = parser.parse_args()


    if not args.prices is None:
        prices = args.prices
    else:
        if prices is None:
            raise Exception("Please give prices")
    if not args.periods is None:
        periods = args.periods

    
    if not periods >= len(prices):
        prices = prices[-periods:]
        n = len(prices)
        prices = np.array(prices)
        deltas = np.diff(prices)
        seed = deltas[:n+1]
        up = seed[seed >= 0].sum()/n
        down = -seed[seed < 0].sum()/n
        rs = up/down
        rsi = np.zeros_like(prices)
        rsi = 100. - 100./(1.+rs)
            
        return rsi
    else:
        raise ValueError("The price list not acceptable for periods")