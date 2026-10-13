#!/usr/bin/python3

import argparse
import re
from collections import Counter



trans_start_dict = {
    "a": "nrstl",
    "e": "nrsdl",
    "i": "nrstc",
    "o": "nrsfu",
    "u": "nrstl",
    "l": "eloy",
    "y" : "aeiou", 
    "w" : "aeih", 
    "v" : "aeiou",
    "h" : "aeo", 
    "j" : "aeiou", 
    "x" : "aeiop", 
    "s" : "aeist", 
    "t" : "aeioh", 
    "m" : "aior", 
    "n" : "aeigd", 
    "r" : "aeios", 
    "d" : "aeo", 
    "z" : "aeiou",
    "g" : "aeioh",
    "c" : "aih",
    "k" : "aeion",
    "q" : "aeiou",
    "b" : "aeu",
    "p" : "aeior",
    "f" : "aeior"
}

trans_word_dict = {
    "a": "nrstl",
    "e": "nrsdl",
    "i": "nrstc",
    "o": "nrsfu",
    "u": "nrstl",
    "l": "aeioy",
    "y" : "aeiou", 
    "w" : "aeioh", 
    "v" : "aeiou",
    "h" : "aeiou", 
    "j" : "aeiou", 
    "x" : "aeiop", 
    "s" : "aeist", 
    "t" : "aeioh", 
    "m" : "aeiou",
    "n" : "aeing", 
    "r" : "aeios", 
    "d" : "aeiou", 
    "z" : "aeiou",
    "g" : "aeioh",
    "c" : "aeioh",
    "k" : "aeion",
    "q" : "aeiou",
    "b" : "aeiou",
    "p" : "aeior",
    "f" : "aeior"
}

def single_gesture(word):
    if not word:
        return False
    a = word[0]
    rest = word[1:]
    if not rest:
        return True
    if rest[0] not in trans_start_dict.get(a, ""):
        return False

    return all(
        b in trans_word_dict.get(a, "")
        for a, b in zip(rest, rest[1:])
    )

def double_gesture(word):
    if single_gesture(word):
        return False
    for i in range(1, len(word)):
        if single_gesture(word[:i]) and single_gesture(word[i:]):
            return True
    return False

def main():
    parser = argparse.ArgumentParser(
        description="Analyze starting-letter and letter-transition frequencies."
    )
    parser.add_argument("file", help="text file to analyze")
    args = parser.parse_args()

    try:
        with open(args.file) as f:
            s = " ".join(line.strip().lower() for line in f)

    except OSError as e:
        parser.error(f"cannot open {args.file!r}: {e}")

    # Turn every sequence of non-letters into a single word separator.
    s =  " " + re.sub(r"[^a-z]+", " ", s).strip() + " "
    words = s.split(" ")

    words = s.split()

    valid_words = sorted(
        set(word for word in words if single_gesture(word)),
        key=lambda word: (len(word), word)
    )
    valid_double_words = sorted(
        set(word for word in words if double_gesture(word)),
        key=lambda word: (len(word), word)
    )


    print(">>>DOUBLE WORDS<<<")
    for word in valid_double_words[-40:]:
        print(word)

    print(">>>SINGLE WORDS<<<")
    for word in valid_words[-40:]:
        print(word)

    print(f"Total words: {len(words)}")
    print(f"Distinct words: {len(set(words))}")
    print(f"Single-gesture words: {len(valid_words)}")
    print(f"Double-gesture words: {len(valid_double_words)}")



if __name__ == "__main__":
    main()
