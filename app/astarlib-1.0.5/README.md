[![Build Status](https://travis-ci.org/initbar/astarlib.svg?branch=master)](https://travis-ci.org/initbar/astarlib)

# astarlib

**astarlib** is a [Cython ("C-Extensions for Python")](https://cython.org) implementation of the [A\* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) on a [graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) or a [2-dimensional polygon space](https://en.wikipedia.org/wiki/Polygon) packaged into a reusable library. It was originally implemented as my [battlesnake.io](https://play.battlesnake.io) bot's navigation system (e.g. finding minimum path around enemy bots).

## Example

To find A\* paths in a 2D polygon, you need to initialize an `aStar()` object with a "map" of the traversing space.

**Note**: all elements of a given `array` will be automatically normalized to boolean states. After normalization, elements that are `True` are considered traversable and `False` are treated as untraversable (e.g. obstacle).

```python
>> from astarlib import aStar
>> area = aStar(array=[
  [1, 1, 1, 1, 1, 1],  # see `normalization`
  [0, 1, 0, 1, 1, 1],
  [0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1],
  [0, 1, 0, 1, 0, 1],
  [0, 0, 1, 1, 1, 1],
])
```

And then simply set the start/destination information to find a valid path and cost of the path. In a [snake game](https://en.wikipedia.org/wiki/Snake_(video_game_genre)), "start" is the head of a snake and "end" is an apple.

```python
>> area.find_path(start=(0, 0), end=(area.height-1, area.width-1))
(
  ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)),
  11
)
```

Since the initial "map" is preserved, you can also invoke `.find_path()` multiple times for different traversal paths.

```python
>> area.find_path(start=(0, 0), end=(0, 1))
(
  ((0, 0), (0, 1)),
  2
)
```

If there is no path, `PathNotFoundException` will be raised.

```python
>> area.find_path(start=(0, 0), end=(1, 0))  # `PathNotFoundException`
```

## Build

Local build for development requires [some dependencies](./setup.py) to compile C extensions.

```bash
~$ make
```

## Installation

For `stable` channel:

```bash
~$ pip install astarlib==1.0.0
```

For `edge` channel:

```bash
~$ # sudo apt install gcc python-dev
~$ pip install git+https://github.com/initbar/astarlib.git
```

## Tests

```bash
~$ # pip install pytest
~$ make test
```

## Documentations

See [documentations](./docs).

## License

**astarlib** is licensed under [MIT License](./LICENSE).
