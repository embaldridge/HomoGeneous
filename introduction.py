from __future__ import division
import numpy as np
import random
import sys
import Chapter1


""" Once upon a time, there was... """

a_special_girl = ['XY'] complete androgen insensitivity syndrome
a_special_guy = ['XY']

some_men = [['m']]*100
some_ladies = [['l']]*100


""" Who lived in ... """
a_town = {'folks': [], 'jobs': [], 'pubs': []}


""" With some ..."""
a_town['folks'] = some_men + some_ladies + [a_special_girl] + [a_special_guy]

a_town['jobs'] = {'butcher': 1, 'baker': 1, 'candlestick_maker': 1, 
                'teacher': 4, 'preacher':1, 'bartender': 2,
                'seamstress': 4, 'student': 100, 'farmer': 100,
                'pillow_fighters': 2, 'barber': 2, 'cooks': 10}

a_town['pubs'] = {'The_Thorny_Rose', 'The_Rosy_Nose', 'The_Horny_Those'}


""" And ..."""

for_as_long_as_anyone_can_remember = range(10**4)

for each_day in for_as_long_as_anyone_can_remember: 
    
    # everybody had equal chances for nearly everything they did
    everyone = len(a_town['folks'])
    chance = 1/everyone # chance won over everyone 
     
    for example in a_town: # like this
         
        we_both_might_want_the_same_job = True # and...
        if we_both_might_want_the_same_job == True:
            
            # and nobody else wants it, then...
            your_chance = 1/2
            my_chance = float(your_chance)
        
            # now, we could fight over it.
            fight = 'why not'
            if fight == 'why not':
                print 'Hello? Golden rule, anyone?'
                
            # or we could draw straws.
            you = np.random.binomial(1, 0.5, 1)
            if you == 1:
                me = 'lose'
                print 'Try again.'
                
             # you get the point
            break         
    break

# Now you've probably noticed that all the men in the town are basically the
# same. Of course, you re right. They were basically the same in every possible
# way. And of course, the same went for the women.
    
""" That is, except for our special girl and special guy. """

# And, if these two had never met, I might not have this story to tell.
# But as it happens, they did...

serendipity = 'wait for it...'
while serendipity == 'wait for it...':
    
    couple = random.sample(a_town['folks'],2)
    if a_special_girl and a_special_guy in couple:
        serendipity = 'yes'
        print 'Girl sees boy.'
        print 'Girl RECOGNIZES boy.' # but didn't we agree that all guys
        # are the same? 
        print 'Boy is terrified.' # apparently, he thought the same thing.
        print 'Boy runs off screaming.'
        break
        
    else: print serendipity,
    
# Of course, you might be freaked out too, if you thought you were living in
# a perfectly equittable society of completely unrecognizable anonymous people!

""" As it happens, there was also a..."""

a_town['folks'].append('Lunatic')

""" And this is where our story starts to ...""" 

def get_interesting(a_town):
    Chapter1.story(a_town)
    return

get_interesting(a_town)
