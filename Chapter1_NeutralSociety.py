from __future__ import division
import numpy as np
import random
import sys
import time
#import Chapter2

def dp(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.05)

dp("\n\nChapter 1: Neutral Society\n")
dp("\nOur anti-hero and he-heroine have just met and you, the")
dp(" ill-informed reader, may still have little idea as to why he ran off. ")
dp("An anonymous society where all folks have equal chances of basically ")
dp("everything? How would that even work?")
