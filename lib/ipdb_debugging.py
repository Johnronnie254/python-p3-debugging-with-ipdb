#!/usr/bin/env python3

import ipdb

def plus_two(num):
    num += 2  # This line adds 2 to num and assigns the result back to num
    ipdb.set_trace()  # This sets a breakpoint for debugging
    return num
