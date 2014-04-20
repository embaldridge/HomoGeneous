from __future__ import division
import numpy as np
import random
import sys
import time


def dp(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.05)

def narrative(a_town):

    dp("\n\nChapter 1: Neutral Society\n")
    dp("\nOur anti-hero and he-heroine have just met and you, the")
    dp(" ill-informed reader, may still have little idea as to why he ran off.\n ")
    dp("An anonymous society where all folks have equal chances of basically ")
    dp("everything?\nHow would that even work?")