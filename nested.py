#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Sean Bailey, Chris Wilson, Joseph Hafed, Janell Huyuck, Kano Marvel, Koren Niles"


import sys


def is_matched(s):
    opn_bracket = []
    index = 0
    answer = "Yes"
    brac_types = {
        "paraspla": ["(*", "*)"],
        "parens": ["(", ")"],
        "squares": ["[", "]"],
        "curlies": ["{", "}"],
        "arrows": ["<", ">"]
    }

    while s:
        index += 1
        if s[:2] == "(*" or s[:2] == "*)":
            token = s[:2]
        else:
            token = s[0]
        for bracket in brac_types:
            if token == brac_types[bracket][0]:
                opn_bracket.append(token)
            if token == brac_types[bracket][-1]:
                if opn_bracket[-1] != brac_types[bracket][0]:
                    answer = "NO " + str(index)
                    token = s
                else:
                    opn_bracket.pop()
        s = s[len(token):]
    if len(opn_bracket) > 0:
        answer = "NO " + str(index)
    return answer


def is_nested(line):
    """Validate a single input line for correct nesting"""
    pass


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    answer = ''
    with open('input.txt', 'r') as rf:
        for s in rf:
            answer += is_matched(s) + '\n'
    with open('output.txt', 'w') as wf:
        wf.write(answer)


if __name__ == '__main__':
    main(sys.argv[1:])
