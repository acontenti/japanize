import difflib
import sys

from janames import janames
from util import rotoni


def japanize(names):
    for it in map(transform, names.split(" ")):
        print(it["romaji"], "(" + it["hiragana"] + ")", end=" ")


def transform(name):
    match = difflib.get_close_matches(name.lower().replace("l", "r"), janames, 1)
    if match:
        return {"romaji": match[0].capitalize(), "hiragana": rotoni(match[0])}
    else:
        return {"romaji": name.capitalize(), "hiragana": rotoni(name)}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    japanize(" ".join(sys.argv[1:]))
