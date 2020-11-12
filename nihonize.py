import sys

VOWELS = "aeiou"


def isvowel(c):
    return c in VOWELS


def nihonize(names):
    for name in names.split(" "):
        last = ""
        result = ""
        for c in name:
            if not last:
                result += c
            else:
                if isvowel(c):
                    if isvowel(last):
                        result += c
                    else:
                        result += c
                else:
                    if isvowel(last):
                        if c == "l":
                            result += "r"
                        else:
                            result += c
                    else:
                        if c != last:
                            if c == "l":
                                result += "ur"
                            else:
                                result += "u" + c
            last = c
        if not isvowel(last):
            result += "u"
        print(result.capitalize(), end=" ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nihonize(" ".join(sys.argv[1:]))
