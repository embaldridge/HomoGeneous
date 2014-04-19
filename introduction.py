from __future__ import division
import numpy as np
import random
import sys
import Chapter1_NeutralSociety as Ch1


print "\nIntroduction: Define some variables\n"

print "For our story, we'll need a",
a_special_girl = ['he-heroine', 'XY'] # with complete androgen insensitivity syndrome
a_special_guy = ['anti-hero','XY']  # with a seriously lacking sense of adventure

print str(a_special_girl[0]) + ', an ' + str(a_special_guy[0])+', and a neutral society.',

print " Like any society, this one will have a town with",
a_town = {'folks': [], 'jobs': [], 'pubs': []}
print a_town.keys(),'.',

anonymous_men = [['m']] * 10000
anonymous_ladies = [['l']] * 10000
a_town['folks'] = anonymous_men + anonymous_ladies + [a_special_girl] + [a_special_guy]

a_town['jobs'] = {'butcher': 2, 'baker': 3, 'candlestick_maker': 2,
                'shopkeeer': 20, 'dentist':4, 'physician':10, 
                'teacher': 100, 'bartender': 6, 'barista': 10,
                'seamstress': 4, 'student': 1000, 'farmer': 100,
                'custodian': 50, 'laborer': 1000, 'hunter': 20,
                'pillow_fighters': 8, 'barber': 4, 'cooks': 100}

a_town['pubs'] = {'Ye Olde Bar', 'The Short Stick', 'The Ball and Urn'}

print """Unlike any society you've heard of among any species of human, all men
look and act the same, as do all women. Likewise, all men and women act as
if there are just men and women. There are no elderly, no infirmed, and the
children are precocious cannibals. But, we'll get to the reproductive biology 
of this curious species of human later. As for now, I'll simply refer to 
them as Homo neutralis (Neutral man) and simply refer you to the source
code.\n"""

for_as_long_as_anyone_can_remember = range(10**4)

for each_day in for_as_long_as_anyone_can_remember: 
    
    everyone = len(a_town['folks'])
    chance = 1/everyone 
    
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
print serendipity
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
        
    
# Of course, you might be freaked out too, if you thought you were living in
# a perfectly equittable society of completely unrecognizable anonymous people!

""" As it happens, there was also a..."""

a_town['folks'].append('Lunatic')

""" And this is where our story starts to ...""" 

def get_interesting(a_town):
    Ch1.story(a_town)
    return

get_interesting(a_town)
