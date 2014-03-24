Game of Life
============
`
##Overview
Game of life is a simple application developed by [John Conway](http://en.wikipedia.org/wiki/Conway's_Game_of_Life). This is an app that simulates the functionality of Game of Life with two simple rules.

1. Any live cell will live in the next round only if it has at least two and at most three live neighbours.
2. A dead cell will live again in the next round if it has exactly three live neighbours.

This simulation brings about interesting that are worth viewing. See for yourself.

##Setup
###Requirements
1. [Python 2.7](https://www.python.org/download/). Check the site for how to install on your computer.

###Run
`cd` into the `game_of_life` directory and type `python ui.py` and enter the percentage of live cells, and the width and height of the torus.
```sh
$ cd game_of_life/
$ python ui.py
Enter the percentage of live cells (Between 1 and 100) > 40
Enter the torus width (An integer) > 20
Enter the torus height (An integer) > 20
```

##Known Issues
No known issues yet. Report issues [here](mailto:gerald@meltwater.org)