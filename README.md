# Transfinite Nim Game

This is a Python implementation of the transfinite Nim game.

In this two-player game, there are several rows, each containing an [ordinal number](https://en.wikipedia.org/wiki/Ordinal_number) of objects. At each turn, the player chooses one of the rows and replaces the number of objects by a strictly lower ordinal number. If all rows are empty, the player who played at last wins.

In this implementation, you play against the computer. You can choose the initial configuration, and the computer begins to play. It plays the winning strategy if there is one (which is often but not always the case), and otherwise it plays stupidly.

## `ordinals.py`

This is a library that implements ordinal numbers and their basic operations. It can only manipulate ordinals below $\varepsilon_0$. Ordinals behave like a superset of the natural integers: you can use the usual operations `+`, `*`, `**`, `<`, `==`, etc. with both integers and ordinals.

![An example of operations between ordinals](ordinals.jpg)

## `nim.py`

This file contains the actual game.

![Beginning of a game](nim.jpg)


## Warning

The program is not foolproof and may contain bugs.
