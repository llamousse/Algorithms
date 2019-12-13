#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  # define list of all possible plays
  plays = ["rock", "paper", "scissors"]

  # output of possible outcomes
  outcomes = []

  # base case (the case you know the answer to)
  if n == 0:
    return [[]]
  if n == 1:
    return [['rock'],['paper'],['scissors']]

  # recursive case
  for x in rock_paper_scissors(n - 1):
    outcomes.append(x + [plays[0]])
    outcomes.append(x + [plays[1]])
    outcomes.append(x + [plays[2]])

  return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')