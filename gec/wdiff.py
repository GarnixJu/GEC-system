# -*- coding: utf-8 -*-
import sys

INSERT_TOKEN = '{{+{0}+}}'
DELETE_TOKEN = '[-{0}-]'


def parse_line(line):
    return line.strip().split()


def find_lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result.insert(0, a[x-1])
            x -= 1
            y -= 1
    return result


def iter_diff_tokens(src, trg, lcs):
    for token in lcs:
        while len(src) > 0 and src[0] != token:
            yield DELETE_TOKEN.format(src.pop(0))
        while len(trg) > 0 and trg[0] != token:
            yield INSERT_TOKEN.format(trg.pop(0))
        yield token
        src.pop(0)
        trg.pop(0)

    # return remaining tokes in source and target
    while len(src) > 0:
        yield DELETE_TOKEN.format(src.pop(0))
    while len(trg) > 0:
        yield INSERT_TOKEN.format(trg.pop(0))


def wdiff(src, trg):
    src, trg = parse_line(src), parse_line(trg)
    lcs = find_lcs(src, trg)
    if not lcs:
        return DELETE_TOKEN.format(' '.join(src)), INSERT_TOKEN.format(' '.join(trg))
    elif len(lcs) == len(src) == len(trg):
        return lcs
    return list(iter_diff_tokens(src, trg, lcs))


def main():
    for src, trg in zip(open(sys.argv[1]), open(sys.argv[2])):
        diff_tokens = wdiff(src, trg)
        if diff_tokens:
            print(' '.join(diff_tokens))


if __name__ == '__main__':
    main()
