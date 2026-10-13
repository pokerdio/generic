#!/usr/bin/python3

import argparse
import re
from collections import Counter

def make_rank(counter):
    ret = {}
    rank = 1
    for key, count in counter.most_common():
        ret[key] = rank
        rank = rank + 1
    return ret

def main():
    parser = argparse.ArgumentParser(
        description="Analyze starting-letter and letter-transition frequencies."
    )
    parser.add_argument("file", help="text file to analyze")
    parser.add_argument(
        "n",
        nargs="?",
        type=int,
        default=100,
        help="number of most common transitions to print (default: 100)"
    )
    args = parser.parse_args()

    if args.n < 1:
        parser.error("n must be a positive integer")

    start_freq = Counter()
    occur_freq = Counter()
    transition_freq = Counter()

    letter_trans_freq = {chr(a):Counter() for a in range(ord("a"), ord("z") + 1)}
    try:
        with open(args.file) as f:
            s = " ".join(line.strip().lower() for line in f)
    except OSError as e:
        parser.error(f"cannot open {args.file!r}: {e}")

    # Turn every sequence of non-letters into a single word separator.
    s =  " " + re.sub(r"[^a-z]+", " ", s).strip() + " "

    for a, b in zip(s, s[1:]):
        if a != " ":
            occur_freq.update([a])
        if b == " ":
            continue
        if a == " ":
            start_freq.update([b])
        else:
            transition_freq.update([a + b])
            letter_trans_freq[a].update([b])

    

    start_rank = make_rank(start_freq)
    occur_rank = make_rank(occur_freq)

    starts_total = start_freq.total()
    transitions_total = transition_freq.total()

    print("Starting letters")
    print("----------------")
    for letter, count in start_freq.most_common():
        occur = occur_freq[letter]
        occur_div = occur / (occur_freq.total() or 1)
        s = f"{letter}: S#{start_rank[letter]} {count / starts_total:0.2%} " + \
            f"O#{occur_rank[letter]} {occur_div:0.2%}-> "
        fr = letter_trans_freq[letter]
        fr_total = fr.total()
        for next_letter, fr_count in fr.most_common(7):
            s = s + f"{next_letter}({fr_count / fr_total:0.2%})"
        print (s)

    print(f"\nTop {args.n} transitions")
    print("-------------------")
    for transition, count in transition_freq.most_common(args.n):
        print(f"{transition}: {count:8,d}  {count / transitions_total:7.3%}")


if __name__ == "__main__":
    main()
