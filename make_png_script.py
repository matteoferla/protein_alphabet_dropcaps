#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """

NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import argparse
from pprint import PrettyPrinter

pp = PrettyPrinter()

cmd='''cd /Users/matteo/Coding/protein alphabet
load AlphabetPDB/{L}.pse
bg_color white
set ray_trace_mode,  3
ray 476, 476
save Alphabet_ray/{L}.png
'''

from string import ascii_uppercase
for letter in ascii_uppercase:
    print(cmd.replace('{L}',letter))