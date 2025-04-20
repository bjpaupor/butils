# BUtils

A collection of utilities written by Brandon, currently limited to:
- AD&D character generation
  - generate.py:

- Dice rolling
  - dice.py

## AD&D Character Generation

Run using `python generate.py`, with an optional command-line argument to select which method of score generation should be used (as described when running without the argument)

## Dice Rolling

Run using `python dice.py`, with an optional command-line argument to describe the roll in XdY format

## TODO

- Display possible classes depending on ancestries for scores that need to be arranged
 - And for the choice of one from twelve
 - Account for ability score 5 or less requirements on class
- Pass by reference cleanup
- Display ancestries and build type(s) that would be valid for given scores, rather than giving invalid responses