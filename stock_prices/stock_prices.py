#!/usr/bin/python

import argparse

prices = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
  # gets all 'sold' stock prices (i.e. buy, sell, buy, sell, etc)
  # stocks_sold_list = prices[1::2]
  # min_value = min(stocks_sold_list)
  # max_value = max(stocks_sold_list)

  max_value = max(prices)
  # max_profit - max_value - 0

  # for x in prices:
  if max_value == prices[0]:
    new_stock_list = prices[1:]
    print(new_stock_list)
    new_max = max(new_stock_list)
    print(new_max)
    if new_max == prices[0]:
      print(max_value)
      max_profit = new_max - max_value
      return max_profit
  else:
    max_value_index = prices.index(max(prices))

    new_stocks_list = prices[0:max_value_index]
    # print(new_stocks_list)

    min_value = min(new_stocks_list)
    new_max_profit = max_value - min_value
    return new_max_profit

  # max_value = max(prices)
  # max_value_index = prices.index(max(prices))

  # new_stocks_list = prices[0:max_value_index]
  # # print(new_stocks_list)

  # min_value = min(new_stocks_list)
  # max_profit = max_value - min_value

  # return max_profit

print(find_max_profit(prices))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))