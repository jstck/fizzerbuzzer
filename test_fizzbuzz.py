import subprocess
import sys

import pytest

from fizzbuzz import DEFAULT_PAIRS, fizzbuzz_line, parse_pairs
from fizzgen import generate

TPB = [(3, "Tomato"), (7, "Potato"), (11, "Banana")]


def test_classic():
    assert [fizzbuzz_line(i, DEFAULT_PAIRS) for i in (1, 3, 5, 15)] == ["1", "Fizz", "Buzz", "FizzBuzz"]


def test_words_in_given_order():
    assert fizzbuzz_line(21, TPB) == "TomatoPotato"
    assert fizzbuzz_line(231, TPB) == "TomatoPotatoBanana"
    assert fizzbuzz_line(231, TPB[::-1]) == "BananaPotatoTomato"


def test_parse_pairs():
    assert parse_pairs(["3", "Fizz", "5", "Buzz"]) == DEFAULT_PAIRS
    assert parse_pairs([]) == []


@pytest.mark.parametrize("args", [["3"], ["3", "Fizz", "5"], ["x", "Fizz"], ["0", "Zero"], ["-3", "Neg"]])
def test_parse_pairs_rejects(args):
    with pytest.raises(ValueError):
        parse_pairs(args)


@pytest.mark.parametrize("pairs", [DEFAULT_PAIRS, TPB, [(2, "it's"), (3, 'say "hi"\\n')]])
def test_generated_script_matches(tmp_path, pairs):
    script = tmp_path / "gen.py"
    script.write_text(generate(pairs))
    out = subprocess.run([sys.executable, script, "120"], capture_output=True, text=True, check=True).stdout
    assert out.splitlines() == [fizzbuzz_line(i, pairs) for i in range(1, 121)]
