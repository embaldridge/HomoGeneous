from __future__ import division
import numpy as np
import random
import sys
import time
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

print """Unlike any society you've heard of, all men in this netural society
look and act the same, as do all women. Nobody recognizes anybody and nobody
wants to. Of course, this sort of anonymous society requires a few caveats.
For example, it's a bit difficult to maintain anonymity if you've got people
using names, owning property, raising families, and holding down stable jobs. 
So, we'll have none of that. Likewise, all men and women act as if there are 
just men and women. There are no elderly, no infirmed, and the children are 
precocious cannibals. We'll get to the reproductive biology of this curious
species of human later. As for now, I'll simply refer to them as Homo neutralis
(Neutral man) and simply refer you to the source code.\n"""

for_as_long_as_anyone_can_remember = range(10**4)

for each_day in for_as_long_as_anyone_can_remember: 
    
    # Everyone woke with the same chance of being or doing whatever they 
    # wanted because everyone relied on the lotteries. 
    
    everyone = len(a_town['folks'])
    chance = 1/everyone 
    
    for example in a_town: # like this
         
        we_both_might_want_the_same_job = True # and...
        if we_both_might_want_the_same_job == True:
            
            # and nobody else wants it, then...
            your_chance = 1/2
            my_chance = float(your_chance)
            total_probability = your_chance + my_chance
            if total_probability > 1.0:
                print "Somebody is kidding themselves."
                sys.exit() # Very nice. You killed the story.
            
            # Now, we could fight over who gets the job.
            fight = 'why not'
            your_health = 1
            my_health = 1
            if fight == 'why not':
                cage_match = [your_health, my_health]
                damage = -0.1
                p = 0.5 # competition symmetry factor
                # Note: if p = 0.5, you and I are equally matched (neutral)
                while min(cage_match) > 0:
                    victim = np.random.binomial(1, p, 1)
                    cage_match[victim] = cage_match[victim] + damage
                
            # or we could just draw straws. 
            you = np.random.binomial(1, 0.5, 1)
            if you == 1:
                me = 'loser'
                # my_health still equals 1
                    
            break # you get the point         
    break

print """So, it seems I've started us out with an incredibly boring and
implausible society of anonymous passivists who go about their days playing
lotteries and shucking financial responsibilties and family values. And so,
I have. In fact, if our he-heroine and anti-hero had never met, I might not a
have much of a story to tell. As it happens, they did...\n"""

serendipity = 'wait for it...'
print serendipity,

while serendipity == 'wait for it...':
    
    couple = random.sample(a_town['folks'],2)
    if a_special_girl and a_special_guy in couple:
        serendipity = 'yes'
        print 'Girl sees boy. Girl RECOGNIZES boy.',
        # but didn't we agree that all guys are the same? 
        print 'Boy is terrified.', # apparently, he thought the same thing.
        print 'Boy runs off screaming.'
        
# Of course, you might be freaked out too, if you thought you were living in
# a perfectly equittable society of completely unrecognizable anonymous people.

time.sleep(0.5)
print "\nAnd as it happens, there was also a Lunatic."
a_town['folks'].append('Lunatic')

""" And this is where our story starts to ...""" 
def get_interesting(a_town):
    Ch1.story(a_town)
    return

get_interesting(a_town)
