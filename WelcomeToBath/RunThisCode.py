from __future__ import division
# -*- coding: utf-8 -*-
import IntroNarrative as C3PO
import numpy as np
import random
import os
import time
import sys

mydir = os.path.expanduser("~/Desktop")
mypath = mydir + "/Repos/HomoGeneous/"

C3PO.Tell_us_a_story()

# There once was a...
HeHeroine = ['he-heroine', 'XY'] # with complete androgen insensitivity syndrome
# and an ...
AntiHero = ['anti-hero','XY']  # with a seriously lacking sense of adventure


# who lived in the...
Village_of_Bath = {'folks': [], 'jobs': [], 'pubs': []}


# Unlike most villages, or even towns and cities, Bath had only
men = [['m']] * (499)
# and ...
ladies = [['l']] * (499)

Village_of_Bath['folks'] = men + ladies + [HeHeroine] + [AntiHero]
Village_of_Bath['jobs'] = {'butcher': 10, 'baker': 10, 'candlestick_maker': 5,
                'shopkeeer': 20, 'dentist':5, 'physician':5, 
                'teacher': 10, 'bartender': 5, 'barista': 5,
                'seamstress': 5, 'student': 200, 'farmer': 100,
                'custodian': 20, 'general labor': 200, 'hunters': 10,
                'pillow_fighters': 10, 'beautician': 20, 'cooks': 40}


# Bath also had some pubs
Village_of_Bath['pubs'] = {'Ye Olde Bar', 'The Short Stick', 'The Ball and Urn'}

# Now...
as_long_as_anyone_can_remember = range(10**4)
for each_day in as_long_as_anyone_can_remember: 
    
    # Everyone woke with the same chance of being or doing whatever they 
    # wanted because everyone relied on lotteries. 
    
    everyone = len(Village_of_Bath['folks'])
    everyones_chance = 1/everyone 
    
    for example in Village_of_Bath:
         
        we_both_might_want_the_same_job = True # and...
        if we_both_might_want_the_same_job == True:
            
            # and nobody else wants it, then...
            your_chance = 1/2
            my_chance = float(your_chance)
            total_probability = your_chance + my_chance
            
            if total_probability > 1.0:
                print "Somebody is kidding themselves."
                sys.exit() 
            
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
            elif fight == 'let\'s be rational':
                you = np.random.binomial(1, 0.5, 1)
                if you == 1:
                    me = 'loser'
                    # my_health still equals 1
                    
            break # I'm sure that you get the point         
    
    
    """ Now that you've read the code, you can see that I've started us out with
        an incredibly odd and implausible society of anonymous passivists who go
        about their days playing lotteries and shucking financial responsibilties and
        family values. Sure, why not start from a low point? Actually, things are about
        to get interesting because our he-heroine and anti-hero are just about to meet.
    """
    
    serendipity = 'wait for it.'    
    lets_keep_tabs = 0
    
    while serendipity == 'wait for it.':
        
        lets_keep_tabs += 1
        #C3PO.says('.', 0.0001)
        
        couple = random.sample(Village_of_Bath['folks'], 2)
        if HeHeroine and AntiHero in couple:
                    
            serendipity = 'Fate strikes.'
            the_chance = (1/everyone) + (1/(everyone - 1))
            
            C3PO.says("\nFate finally strikes with a probability of "+str(the_chance)+'. ')
            time.sleep(0.8)
            
            likewise = 1/the_chance
            
            C3PO.says('This means a one in '+str(likewise)+' chance that ')
            C3PO.says('whenever two people meet, that it will be our')
            C3PO.says(' he-heroine and anti-hero. ')
            time.sleep(0.5)
            C3PO.says('But it took '+str(lets_keep_tabs))
            C3PO.says(' random encounters for these two to meet. ')
            time.sleep(0.5)
            C3PO.says('Well, that doesn\'t add up! ', 0.1)
            time.sleep(0.5)
            C3PO.says('Of course, that was just a single random encounter ', 0.1)
            time.sleep(0.5)
            C3PO.says('Let\'s see what happens with, oh, a thousand random encounters.')
            time.sleep(0.5)       
            C3PO.says("  INITIATING RANDOM SAMPLING...\n\n", 0.12)
            
            results = [] 
            lets_keep_tabs = 0
            
            while len(results) < 1000:
                #C3PO.says('.', 0.0001)
                lets_keep_tabs += 1
                couple = random.sample(Village_of_Bath['folks'], 2)
                
                if HeHeroine and AntiHero in couple:    
                    results.append(lets_keep_tabs)
                    lets_keep_tabs = 0
            
            result = np.mean(results)
            C3PO.says('Alright, it took, on average, '+str(result)+' random ')
            C3PO.says('encounters until our he-heroine and anti-hero met. ') 
            C3PO.says('A clearer demonstration of our neutral society and how all individuals have equal chances of basically everything,')
            C3PO.says(' but also of how equal chances rarely ever produce equal outcomes. ')
            
            import Intro_Dialogue
            Intro_Dialogue.HeSaysSheSays()
                    
                    
    sys.path.append(mypath+'Ch1_NeutralSociety')
    import Chapter1_NeutralSociety as ch1
    ch1.narrative(Village_of_Bath)
    
    break