#!/usr/bin/python

# NOTES
# keys - ingredient names
# values - ingredient amounts
# ingredients dictionary - amounts available to use

# TODO
# output max number of whole batches that can be made 
# for supplied recipe using available ingredients

import math

def recipe_batches(recipe, ingredients):

  # set temp var to replace later
  temp_batch = 500

# check if length of ingredients is enough for length of recipe
  if len(ingredients) < len(recipe):
    return 0

# loop ingredients list in recipe
# search: iterate through dictionary (key, value)
# key - ingredient name, value - ingredient amount
  for key, value in recipe.items():
    
    # divide each ingredient amount into recipe value
    current_batch = ingredients[key] // value

    # check if current_batch is less than temp_batch
    # finding the lowest available batch which is the maximum batch
    if temp_batch > current_batch:
      temp_batch = current_batch

  batch = temp_batch

  return batch

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))