# fizzerbuzzer

Two small tools around FizzBuzz, using only the Python standard library.

## `fizzbuzz.py`: generic FizzBuzz

```
./fizzbuzz.py [N [F1 W1 [F2 W2 ...]]]
```

Counts from 1 to `N` (default 100). Each number prints the word of every factor that divides it, in the order given, or the number itself if none do. With no factor/word pairs it runs the classic 3=Fizz, 5=Buzz.

```sh
./fizzbuzz.py                                   # classic, up to 100
./fizzbuzz.py 30                                # classic, up to 30
./fizzbuzz.py 100 3 Tomato 7 Potato 11 Banana   # 21 -> TomatoPotato
```

## `fizzgen.py`: FizzBuzz script generator

```
./fizzgen.py [-o OUTFILE] [F1 W1 [F2 W2 ...]]
```

Generates a short standalone script hardcoded to the given pairs (default 3=Fizz, 5=Buzz). Without `-o` the script goes to stdout. With `-o` it's written to that file and made executable. The generated script takes the upper bound as its only argument (default 100).

```sh
./fizzgen.py -o tpb.py 3 Tomato 7 Potato 11 Banana
./tpb.py 50
```

## Tests

```sh
pip install pytest
pytest
```
