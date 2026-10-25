#!/usr/bin/env python3
"""FizzBuzz script generator.

Usage: fizzgen.py [-o OUTFILE] [F1 W1 [F2 W2 ...]]

Generates a compact standalone Python script that does FizzBuzz with the given
factor/word pairs (default 3=Fizz, 5=Buzz). The generated script takes the
upper bound as its only argument (default 100). Writes to stdout unless -o is
given, in which case the file is written and made executable.
"""
import os
import sys

from fizzbuzz import DEFAULT_BOUND, DEFAULT_PAIRS, parse_pairs

USAGE = "usage: fizzgen.py [-o OUTFILE] [F1 W1 [F2 W2 ...]]"


def generate(pairs):
    # str * bool gives the word or "", and an all-empty result falls back to i
    words = " + ".join(f"{word!r} * (i % {f} == 0)" for f, word in pairs)
    return (
        "#!/usr/bin/env python3\n"
        "import sys\n"
        f"for i in range(1, int(sys.argv[1]) + 1 if len(sys.argv) > 1 else {DEFAULT_BOUND + 1}):\n"
        f"    print({words} or i)\n"
    )


def main(argv):
    argv = list(argv)
    outfile = None
    try:
        if "-o" in argv:
            idx = argv.index("-o")
            if idx + 1 >= len(argv):
                raise ValueError("-o needs a filename")
            outfile = argv.pop(idx + 1)
            argv.pop(idx)
        pairs = parse_pairs(argv) or DEFAULT_PAIRS
    except ValueError as e:
        print(f"error: {e}\n{USAGE}", file=sys.stderr)
        sys.exit(2)
    code = generate(pairs)
    if outfile is None:
        sys.stdout.write(code)
    else:
        with open(outfile, "w") as fh:
            fh.write(code)
        os.chmod(outfile, os.stat(outfile).st_mode | 0o111)


if __name__ == "__main__":
    main(sys.argv[1:])
