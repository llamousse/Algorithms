#!/usr/bin/python

import argparse

# prices = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
  # set initial min_profit if max is prices[0]
  current_min_profit = prices[0]
  
  # set initial max_profit computed by subtracting 1 - 0
  current_max_profit = prices[1] - prices[0]

  # loop prices list starting at prices[1]
  for x in range(1, len(prices)):
    # if there's a # in prices lower than min_profit
    if prices[x] < current_min_profit:
      current_min_profit = prices[x]
    # else if difference between current price & min_profit 
    # is greater than max_profit, set new max_profit
    elif current_max_profit < prices[x] - current_min_profit:
      current_max_profit = prices[x] - current_min_profit
  
  # set current_max_profit to the final max_profit calculated
  max_profit = current_max_profit

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))