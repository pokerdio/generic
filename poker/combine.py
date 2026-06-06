#!/usr/bin/env python3
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} OUTFILE INFILE...", file=sys.stderr)
        sys.exit(1)

    outname = sys.argv[1]
    infiles = sys.argv[2:]

    totals = defaultdict(lambda: [0, 0, 0])

    for fname in infiles:
        with open(fname, "rt") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split()
                if len(parts) != 5:
                    raise ValueError(f"{fname}:{lineno}: expected 5 fields, got {len(parts)}: {line!r}")

                h1, h2, w, l, t = parts
                key = (h1, h2)

                totals[key][0] += int(w)
                totals[key][1] += int(l)
                totals[key][2] += int(t)

    with open(outname, "wt") as out:
        for h1, h2 in sorted(totals):
            w, l, t = totals[(h1, h2)]
            out.write(f"{h1} {h2} {w} {l} {t}\n")

if __name__ == "__main__":
    main()
