#!/usr/bin/env python3
"""Generic FizzBuzz.

Usage: fizzbuzz.py [N [F1 W1 [F2 W2 ...]]]

Counts from 1 to N (default 100). For each number, prints the words of all
factors that divide it, in the order given, or the number itself if none do.
Without factor/word pairs, runs the classic 3=Fizz, 5=Buzz.
"""
import sys

DEFAULT_BOUND = 100
DEFAULT_PAIRS = [(3, "Fizz"), (5, "Buzz")]
USAGE = "usage: fizzbuzz.py [N [F1 W1 [F2 W2 ...]]]"


def parse_pairs(args):
    """Turn ["3", "Fizz", "5", "Buzz"] into [(3, "Fizz"), (5, "Buzz")]."""
    if len(args) % 2:
        raise ValueError(f"factor {args[-1]!r} has no word")
    pairs = []
    for factor, word in zip(args[::2], args[1::2]):
        try:
            f = int(factor)
        except ValueError:
            raise ValueError(f"factor {factor!r} is not an integer") from None
        if f < 1:
            raise ValueError(f"factor {f} must be a positive integer")
        pairs.append((f, word))
    return pairs


def fizzbuzz_line(i, pairs):
    return "".join(word for f, word in pairs if i % f == 0) or str(i)


def main(argv):
    try:
        bound = int(argv[0]) if argv else DEFAULT_BOUND
        pairs = parse_pairs(argv[1:]) or DEFAULT_PAIRS
    except ValueError as e:
        print(f"error: {e}\n{USAGE}", file=sys.stderr)
        sys.exit(2)
    for i in range(1, bound + 1):
        print(fizzbuzz_line(i, pairs))


if __name__ == "__main__":
    main(sys.argv[1:])
